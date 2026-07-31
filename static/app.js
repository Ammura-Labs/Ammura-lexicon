const script = document.querySelector('#script');
const counter = document.querySelector('#word-count');
const file = document.querySelector('#script_file');
if (script && counter) { const update = () => { const count = script.value.trim() ? script.value.trim().split(/\s+/).length : 0; counter.textContent = `${count.toLocaleString()} word${count === 1 ? '' : 's'}`; }; script.addEventListener('input', update); update(); }
if (file && script) file.addEventListener('change', () => { if (file.files[0]) { script.required = false; document.querySelector('.upload-zone strong').textContent = file.files[0].name; } });
