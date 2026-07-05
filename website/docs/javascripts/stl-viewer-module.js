import * as THREE from "https://esm.sh/three@0.160.0";
import { OrbitControls } from "https://esm.sh/three@0.160.0/examples/jsm/controls/OrbitControls.js";
import { STLLoader } from "https://esm.sh/three@0.160.0/examples/jsm/loaders/STLLoader.js";

function initViewer(container) {
  const status = document.createElement("div");
  status.className = "stl-status";
  status.textContent = "Loading model...";
  container.appendChild(status);

  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.setSize(container.clientWidth, container.clientHeight, false);
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  container.appendChild(renderer.domElement);

  const scene = new THREE.Scene();
  const bgAttr = (container.getAttribute("data-bg") || "").trim().toLowerCase();
  if (bgAttr === "transparent") {
    renderer.setClearAlpha(0);
    scene.background = null;
  } else {
    const bg =
      container.getAttribute("data-bg") ||
      getComputedStyle(container).backgroundColor ||
      "#111111";
    renderer.setClearAlpha(1);
    scene.background = new THREE.Color(bg);
  }

  const camera = new THREE.PerspectiveCamera(
    45,
    Math.max(container.clientWidth, 1) / Math.max(container.clientHeight, 1),
    0.1,
    10000
  );

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.08;
  controls.enablePan = true;
  controls.autoRotate = container.getAttribute("data-autorotate") === "true";
  controls.autoRotateSpeed = 0.0;

  scene.add(new THREE.HemisphereLight(0xffffff, 0x444444, 0.85));
  const dir = new THREE.DirectionalLight(0xffffff, 0.8);
  dir.position.set(1, 1, 1);
  scene.add(dir);

  if (container.getAttribute("data-grid") === "true") {
    const size = parseFloat(container.getAttribute("data-grid-size") || "1000");
    const divisions = parseInt(container.getAttribute("data-grid-divisions") || "20", 10);
    const color1 = new THREE.Color(container.getAttribute("data-grid-color1") || "#333333");
    const color2 = new THREE.Color(container.getAttribute("data-grid-color2") || "#222222");
    const gridY = parseFloat(container.getAttribute("data-grid-y") || "-0.001");
    const grid = new THREE.GridHelper(size, divisions, color1, color2);
    grid.position.y = gridY;
    scene.add(grid);
  }

  const srcAttr = container.getAttribute("data-src");
  if (!srcAttr) {
    status.textContent = "Missing data-src";
    return;
  }
  const src = new URL(srcAttr, document.baseURI).href;

  function fitCameraToSphere(cam, ctrls, radius, offset = 1.35) {
    const vFov = THREE.MathUtils.degToRad(cam.fov);
    const hFov = 2 * Math.atan(Math.tan(vFov / 2) * cam.aspect);
    const distV = radius / Math.sin(vFov / 2);
    const distH = radius / Math.sin(hFov / 2);
    const dist = Math.max(distV, distH) * offset;

    const dir = new THREE.Vector3(1, 1, 1).normalize();
    cam.position.copy(ctrls.target).addScaledVector(dir, dist);

    cam.near = Math.max(radius / 1000, 0.01);
    cam.far = dist + radius * 10;
    cam.updateProjectionMatrix();
    cam.lookAt(ctrls.target);
    ctrls.update();
  }

  const loader = new STLLoader();
  loader.load(
    src,
    geometry => {
      geometry.computeVertexNormals();

      const color = new THREE.Color(container.getAttribute("data-color") || "#aaaaaa");
      const metalness = parseFloat(container.getAttribute("data-metalness") || "0.1");
      const roughness = parseFloat(container.getAttribute("data-roughness") || "0.7");

      const mesh = new THREE.Mesh(
        geometry,
        new THREE.MeshStandardMaterial({ color, metalness, roughness })
      );
      scene.add(mesh);

      mesh.rotation.set(
        THREE.MathUtils.degToRad(0),
        THREE.MathUtils.degToRad(90),
        THREE.MathUtils.degToRad(0)
      );

      const boxA = new THREE.Box3().setFromObject(mesh);
      const center = boxA.getCenter(new THREE.Vector3());
      mesh.position.sub(center);

      const boxB = new THREE.Box3().setFromObject(mesh);
      mesh.position.x -= 10;
      mesh.position.y -= boxB.min.y;

      const boxC = new THREE.Box3().setFromObject(mesh);
      const sphere = boxC.getBoundingSphere(new THREE.Sphere());
      controls.target.set(0, 0, 0);
      fitCameraToSphere(camera, controls, Math.max(sphere.radius, 1e-6), 1.35);

      status.textContent = "Drag to rotate, scroll to zoom";
      start();
    },
    xhr => {
      if (xhr.total) {
        const pct = Math.round((xhr.loaded / xhr.total) * 100);
        status.textContent = "Loading " + pct + "%";
      }
    },
    err => {
      status.textContent = "Failed to load STL";
      console.error("STL load error:", err);
    }
  );

  const resize = () => {
    const w = Math.max(container.clientWidth, 1);
    const h = Math.max(container.clientHeight, 1);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h, false);
  };
  new ResizeObserver(resize).observe(container);

  let running = false;
  function animate() {
    if (!running) return;
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
  }
  function start() { if (!running) { running = true; animate(); } }
  function stop() { running = false; }

  new IntersectionObserver(
    entries => entries.forEach(e => (e.isIntersecting ? start() : stop())),
    { root: null, threshold: 0.05 }
  ).observe(container);
}

function initAll() {
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        initViewer(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { rootMargin: "200px" });

  document.querySelectorAll(".stl-viewer").forEach(container => {
    observer.observe(container);
  });
}

if (window.document$ && window.document$.subscribe) {
  window.document$.subscribe(() => { initAll(); });
} else {
  document.addEventListener("DOMContentLoaded", initAll);
}
