---
title: "Field Robot Road Detection & Control"
description: "Implemented camera-based road-boundary detection and decision logic on a Raspberry Pi, sending control commands to an Arduino for mobile robot steering and motion."
date: "2026-11-08"
dateVerified: false
author: "jaja"
projectCategory: "robotics"
tags: ["robotics"]
technologies: ["Python", "OpenCV", "Raspberry Pi", "Arduino", "Motor Control"]
order: 60
featured: false
showOnHome: true
cover: "https://drive.google.com/thumbnail?id=1J7XjttA6vnk38mEErxtXxbbaXc_Og0WA"
coverAlt: "Source project image for Field Robot Road Detection & Control"
resources: [{"label": "Original Project Image (Google Drive)", "url": "https://drive.google.com/thumbnail?id=1J7XjttA6vnk38mEErxtXxbbaXc_Og0WA"}]
---

<!-- Source: MyWeb.xlsx / MyProject rows 18. Markdown is the canonical published content. -->

## Overview

This field robotics project connects camera-based road-boundary detection with the control of a mobile robot.

## Implementation

Python and OpenCV run image processing and decision logic on a Raspberry Pi, which acts as the upper-level controller. The system detects the road boundaries on both sides and sends the resulting control decisions to an Arduino. The Arduino acts as the lower-level controller for drivers and motors.

The source does not identify the communication protocol, camera model, or field-test performance, so those details are left unspecified.

## Technologies

Python, OpenCV, Raspberry Pi, Arduino, image processing, and motor control.
