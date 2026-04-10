# AI Traffic Signal Automation

This project is a real-time traffic signal control system developed using computer vision and AI techniques.

## Overview
The system detects vehicles from video input and dynamically adjusts traffic signals based on traffic density. It also includes an emergency vehicle detection system that prioritizes signal flow.

## Features
- Real-time vehicle detection using OpenCV and YOLO
- Density-based traffic signal control
- Emergency vehicle detection with automatic override
- Adaptive signal timing system

## Technologies Used
- Python
- OpenCV
- YOLO (Object Detection)
- Flask (Web Interface)

## Description
The system processes video input, detects vehicles in real time, and calculates traffic density. Based on the density, it automatically adjusts signal timing to improve traffic flow. In emergency situations, the system overrides normal signals to prioritize emergency vehicles.

## Note
This repository contains a simplified version of the project for demonstration purposes.

## Output
The system successfully detects vehicles in real time and dynamically adjusts traffic signals based on density. Emergency vehicle detection triggers immediate signal override to ensure priority passage.
