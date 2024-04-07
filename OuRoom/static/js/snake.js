const canvas = document.getElementById('game');
const context = canvas.getContext('2d'); // 2D rendering context

const grid = 16;
let count = 0;
let score = 0;
let oldScore = 0;

const snake = {
  x: 160,
  y: 160,
  dx: grid, // Start moving
  dy: 0,    // right horizontally
  cells: [],
  maxCells: 4
};

const apple = {
  x: 320,
  y: 320
};

// Function to generate random int number
const getRandomInt = (min, max) => Math.floor(Math.random() * (max - min)) + min;

// Main loop
function loop() {
  requestAnimationFrame(loop);

  // Slowing down game loops to 15FPS
  if (++count < 4) {
    return;
  }

  count = 0;
  context.clearRect(0, 0, canvas.width, canvas.height); // clears part of the canvas

  // Moving the snake
  snake.x += snake.dx;
  snake.y += snake.dy;

  // Border the position of the snake horizontally and vertically
  snake.x = (snake.x < 0) ? canvas.width - grid : snake.x % canvas.width;
  snake.y = (snake.y < 0) ? canvas.height - grid : snake.y % canvas.height;

  // position snake tracking
  snake.cells.unshift({x: snake.x, y: snake.y});
  if (snake.cells.length > snake.maxCells) {
    snake.cells.pop();
  }

  // Drawing point
  context.fillStyle = 'red';
  context.fillRect(apple.x, apple.y, grid - 1, grid - 1);

  // Drawing snake
  context.fillStyle = 'green';
  snake.cells.forEach((cell, index) => {
    context.fillRect(cell.x, cell.y, grid - 1, grid - 1);
    // Checking if the snake ate the point
    if (cell.x === apple.x && cell.y === apple.y) {
      snake.maxCells++;
      score++;
      document.getElementById('score').innerText = 'Wynik: ' + score;
      apple.x = getRandomInt(0, 25) * grid;
      apple.y = getRandomInt(0, 25) * grid;
    }
    // Collision checking
    for (let i = index + 1; i < snake.cells.length; i++) {
      if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
        resetGame();
      }
    }
  });
}


function resetGame() {
  snake.x = 160;
  snake.y = 160;
  snake.cells = [];
  snake.maxCells = 4;
  snake.dx = grid;
  snake.dy = 0;
  apple.x = getRandomInt(0, 25) * grid;
  apple.y = getRandomInt(0, 25) * grid;
  oldScore = score
  document.getElementById('oldscore').innerText = 'Poprzedni wynik: ' + oldScore
  score = 0;
  document.getElementById('score').innerText = 'Wynik: 0';
}


document.addEventListener('keydown', (e) => {

  if (e.which === 37 && snake.dx === 0) { // Left
    snake.dx = -grid;
    snake.dy = 0;
  } else if (e.which === 38 && snake.dy === 0) { // Up
    snake.dy = -grid;
    snake.dx = 0;
  } else if (e.which === 39 && snake.dx === 0) { // Right
    snake.dx = grid;
    snake.dy = 0;
  } else if (e.which === 40 && snake.dy === 0) { // Down
    snake.dy = grid;
    snake.dx = 0;
  }
});

requestAnimationFrame(loop);
