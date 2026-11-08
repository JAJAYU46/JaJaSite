---
title: "Autonomous Navigation & Object Search"
description: "Built an indoor exploration and navigation pipeline that uses a trained YOLO detector to find a target image and navigates toward its location with mapping, localization, and path planning."
date: "2026-11-08"
dateVerified: false
author: "jaja"
projectCategory: "robotics"
tags: ["robotics"]
technologies: ["YOLO", "SLAM", "Localization", "Navigation", "RRT"]
order: 30
featured: true
showOnHome: false
featuredOrder: 3
youtubeUrl: "https://www.youtube.com/playlist?list=PLYVkuRLVSj2VRustcw-vZm7mXflJBX_HD"
cover: "https://drive.google.com/thumbnail?id=13crIqDnknShLcWaorVXfxRoiGhUkQlqX"
coverAlt: "Source project image for Autonomous Navigation & Object Search"
youtubeLabel: "Object-search demonstration playlist"
resources: [{"label": "Object-Search Demonstration Playlist", "url": "https://www.youtube.com/playlist?list=PLYVkuRLVSj2VRustcw-vZm7mXflJBX_HD"}, {"label": "Explanatory Presentation", "url": "https://youtu.be/LMYQcKOfj8E"}, {"label": "Original Project Image (Google Drive)", "url": "https://drive.google.com/thumbnail?id=13crIqDnknShLcWaorVXfxRoiGhUkQlqX"}]
---

<!-- Source: MyWeb.xlsx / MyProject rows 9. Markdown is the canonical published content. -->

## Overview

This indoor target-search project was developed in a mock living-room environment. The robot explores using known map information, searches for a Pikachu target image placed at varying locations, and navigates toward the detected target.

## Technical Focus

- Object detection
- Autonomous exploration
- Mapping and localization
- RRT path planning
- Integrated navigation pipeline

## System Architecture

The project connects target-object detection with exploration, mapping, localization, and navigation. RRT path planning is part of the technical scope. The demonstration playlist provides the available visual reference.

## Implementation

1. Sample room images and train a YOLO model to recognize the target image.
2. Use map information and localization to support exploration of the room.
3. Detect the target during exploration.
4. Combine the target location with navigation and path planning, including the documented RRT scope, to move toward it.

The project materials include a demonstration playlist and a separate explanatory presentation. They do not provide verified detection accuracy, navigation success rates, or an explicit breakdown of individual responsibilities.
