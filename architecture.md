# Architecture Overview

## Mobile App
- Built with React Native (Expo)
- Captures camera frames
- Sends optional data to backend
- Displays visual + sound alerts

## Backend (Python)
- FastAPI service
- Processes
 frames or sensor data
- Runs ML fatigue-detection models

## ML Layer
- Placeholder for future:
  - Eye-blink detection
  - Yawning detection
  - Head-position analysis
