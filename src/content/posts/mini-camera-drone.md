---
title: "Mini Camera Drone Development"
description: "A camera-drone prototype combining a laser-cut frame, an ESP32-CAM wireless video feed, and iterative motor-control circuitry, with documented weight and thermal constraints."
date: "2026-11-08"
dateVerified: false
author: "jaja"
projectCategory: "embedded"
tags: ["embedded"]
technologies: ["SolidWorks", "Laser Cutting", "ESP32-CAM", "Arduino", "MOSFET", "Circuit Prototyping", "Arduino IDE", "App Inventor", "H-bridge Drivers"]
order: 130
featured: false
showOnHome: false
cover: "https://drive.google.com/thumbnail?id=1-hlYLf3wN2HiTVVr3u4Xdfr9z4Zg0Wkc"
coverAlt: "Source project image for Mini Camera Drone Development"
resources: [{"label": "Original Project Image (Google Drive)", "url": "https://drive.google.com/thumbnail?id=1-hlYLf3wN2HiTVVr3u4Xdfr9z4Zg0Wkc"}]
gallery: [{"url": "https://drive.google.com/thumbnail?id=10BYENVyNXnrGwI_Z3ByJAQ5bsMoGpQqO", "alt": "ESP32-CAM camera system (individual work)", "caption": "ESP32-CAM camera system (individual work)"}, {"url": "https://drive.google.com/thumbnail?id=10FUUjPDN9r59T0N72dFyOmaFqBv39M7a", "alt": "Initial Arduino Nano / H-bridge circuit (team work)", "caption": "Initial Arduino Nano / H-bridge circuit (team work)"}, {"url": "https://drive.google.com/thumbnail?id=10WlH2fWZvBOakmg73StH1zxrFGlp1c6T", "alt": "MOSFET circuit iteration (team work)", "caption": "MOSFET circuit iteration (team work)"}, {"url": "https://drive.google.com/thumbnail?id=1J2gI1AZ3Xco88vp0XkqEro_X390jtTAX", "alt": "Soldered perfboard circuit iteration (team work)", "caption": "Soldered perfboard circuit iteration (team work)"}]
---

<!-- Source: MyWeb.xlsx / MyProject rows 20, 21, 22, 23, 24. Markdown is the canonical published content. -->

## Overview

This small camera-drone prototype was prepared for an NTU Azalea Festival exhibit in February 2023. Five original project records are consolidated here: individual frame and camera-system work, followed by three stages of team circuit development.

## Frame Design

I designed the frame in SolidWorks, cut wooden components with a laser cutter, and assembled the snap-fit structure. Laser kerf reduced the cut dimensions relative to the drawings, which led to loose fits during operation. I adjusted the slot dimensions and standardized the wood material to improve the fit.

## ESP32-CAM Video System

I connected an ESP32-CAM to a local wireless network so devices on that network could access its image stream by IP address. An App Inventor mobile app retrieved and displayed the stream. This camera-system work is identified as individual work in the original record.

## Motor Control Circuit

Circuit development was team work, with three documented iterations:

1. **Arduino Nano and H-bridges:** A small breadboard connected an Arduino Nano to two H-bridge drivers to control four propeller motors.
2. **MOSFET-based control:** The team replaced the heavier H-bridge arrangement with MOSFETs. High-current operation caused overheating; heatsinks and thicker battery leads were added to address heat and current handling.
3. **Soldered perfboard:** The team replaced the breadboard with soldered perfboard to reduce weight.

## Engineering Challenges

Mechanical tolerances, circuit mass, battery placement, current handling, and thermal management all affected the prototype. The original account reports that placing the battery beneath the frame allowed it to lift off, while the intended flight-control goals were not achieved because of weight constraints.

This work is a prototype and integration exercise. It is not evidence of completed autonomous flight or a validated flight-control system.

## Technologies

SolidWorks, laser cutting, ESP32-CAM, Arduino Nano, Arduino IDE, App Inventor, H-bridge drivers, MOSFETs, soldering, and circuit prototyping.
