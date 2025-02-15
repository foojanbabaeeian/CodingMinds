const canvas = document.getElementById('paintCanvas');
const ctx = canvas.getContext('2d');
const brushSizeInput = document.getElementById('brushSize');
const brushColorInput = document.getElementById('brushColor');
const clearButton = document.getElementById('clearCanvas');

// Set up canvas
canvas.width = window.innerWidth * 0.8;
canvas.height = window.innerHeight * 0.8;
ctx.lineCap = 'round';

let isDrawing = false;
let brushSize = brushSizeInput.value;
let brushColor = brushColorInput.value;
let lastX = 0;
let lastY = 0;

// Update brush size and color
brushSizeInput.addEventListener('input', () => {
  brushSize = brushSizeInput.value;
});
brushColorInput.addEventListener('input', () => {
  brushColor = brushColorInput.value;
});

// Clear canvas
clearButton.addEventListener('click', () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
});

// Start drawing
canvas.addEventListener('mousedown', (e) => startDrawing(e.offsetX, e.offsetY));
canvas.addEventListener('mousemove', (e) => draw(e.offsetX, e.offsetY));
canvas.addEventListener('mouseup', () => isDrawing = false);
canvas.addEventListener('mouseout', () => isDrawing = false);

canvas.addEventListener('touchstart', (e) => {
  const touch = e.touches[0];
  startDrawing(touch.clientX - canvas.offsetLeft, touch.clientY - canvas.offsetTop);
});
canvas.addEventListener('touchmove', (e) => {
  const touch = e.touches[0];
  draw(touch.clientX - canvas.offsetLeft, touch.clientY - canvas.offsetTop);
});
canvas.addEventListener('touchend', () => isDrawing = false);

// Drawing functions
function startDrawing(x, y) {
  isDrawing = true;
  [lastX, lastY] = [x, y];
}

function draw(x, y) {
  if (!isDrawing) return;
  ctx.strokeStyle = brushColor;
  ctx.lineWidth = brushSize;
  ctx.beginPath();
  ctx.moveTo(lastX, lastY);
  ctx.lineTo(x, y);
  ctx.stroke();
  [lastX, lastY] = [x, y];
}
