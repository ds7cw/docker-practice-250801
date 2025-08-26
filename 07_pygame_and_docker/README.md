
# Containerized Pygame

### Overview
- A menu screen (Start, Quit)
- A classic Tetris playfield centered
- A right-hand side panel showing live score and controls
- Score increments when lines are cleared
- Dockerization so you can run it in a container and stop the container by pressing Quit

<img width="580" height="677" alt="pygame-tetris" src="https://github.com/user-attachments/assets/e7a4889b-a4c3-4ad0-9a7a-279d6800954b" />

GUI apps in containers need access to a display. The Docker setup in this project covers common ways to run Pygame via a host display (X11).

### File structure
Python files:
```bash
07_pygame_and_docker/
├── main.py        # Game loop & event handling
├── settings.py    # Constants & configuration
├── shapes.py      # Shape definitions & rotations
├── piece.py       # Piece class: movement & rotation
├── board.py       # Grid state
└── utils.py       # Helper functions (timing, score format, etc.)
```

All files:
```bash
07_pygame_and_docker/
├── board.py
├── main.py
├── piece.py
├── settings.py
├── shapes.py
├── utils.py
├── requirements.txt
└── Dockerfile
```

### Linux (X11) setup
- Build image: `docker build -t pygame-tetris .` 
- Allow local Docker to use your X server:
  Bash/zsh: `xhost +local:docker`
- Run container with X11 forwarding
  ```bash
  docker run --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
  --name tetris \
  pygame-tetris
  ```
- The GUI should pop up. Click Start to play; Quit exits and stops the container.
- To revoke X access:
  Bash/zsh:  ```xhost -local:docker```
