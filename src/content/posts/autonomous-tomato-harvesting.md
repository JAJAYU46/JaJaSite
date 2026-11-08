---
title: "Autonomous Tomato Harvesting with Next-Best-View Planning"
description: "A robotic perception and Next-Best-View planning pipeline that uses depth-camera point clouds, YOLO, ICP, and OctoMap to guide a manipulator toward clearer views of partially occluded tomatoes."
date: "2026-11-08"
dateVerified: false
author: "jaja"
projectCategory: "robotics"
tags: ["robotics"]
technologies: ["ROS 2", "YOLOv8", "RGB-D", "ICP", "OctoMap", "Ray Casting", "Docker", "Robot Arm", "Gazebo", "DeepSORT", "Open3D", "Signed Distance Fields"]
order: 20
featured: true
showOnHome: false
featuredOrder: 2
youtubeUrl: "https://youtu.be/FapvpN5wpkc"
cover: "https://drive.google.com/thumbnail?id=1ondk1BARA9rqjXV9rQWgMWPY80q7iw43"
coverAlt: "Source project image for Autonomous Tomato Harvesting with Next-Best-View Planning"
youtubeLabel: "ACPA11 research presentation"
resources: [{"label": "Full Project Report", "url": "https://drive.google.com/file/d/1fQugP5H3UlYT9QG-rZcHBkgtyob6sIOC/view?usp=sharing"}, {"label": "ACPA11 Research Presentation", "url": "https://youtu.be/FapvpN5wpkc"}, {"label": "Original Project Image (Google Drive)", "url": "https://drive.google.com/thumbnail?id=1ondk1BARA9rqjXV9rQWgMWPY80q7iw43"}]
---

<!-- Source: MyWeb.xlsx / MyProject rows 7. Markdown is the canonical published content. -->

## Overview

Partially occluded tomatoes can be difficult to observe from a single camera position. This research project connects robotic perception with Next-Best-View (NBV) planning so a manipulator can move from an obstructed initial view toward a clearer view for harvesting.

## Technical Focus

- Next-Best-View algorithm
- Robot perception and 3D reconstruction
- Viewpoint planning
- Robot arm integration
- Research presentation at ACPA11

## System Architecture

The project connects RGB-D perception and 3D reconstruction with Next-Best-View planning and robot arm integration. YOLO, ICP, OctoMap, and ray casting form the technical scope; the public report documents the node responsibilities and viewpoint-evaluation approach summarized below.

## Implementation

The publicly readable project report describes a ROS 2 Humble system running on an ARM64 Ubuntu / Jetson Orin platform. Seven nodes handle depth-cloud preprocessing, tomato detection, point-cloud filtering and registration, OctoMap conversion, NBV calculation, arm motion, and process coordination.

- **Detection and tracking:** YOLOv8 identifies ripe tomatoes, and DeepSORT maintains target identities as the camera moves.
- **Geometry reconstruction:** Observed depth points are filtered against the detected tomato. Open3D registration combines RANSAC initialization with ICP refinement to align a full tomato model to the partial observation.
- **Viewpoint planning:** OctoMap ray casting and signed distance fields evaluate candidate views around the target. The selected pose is passed to the arm controller to move the end-effector camera toward a clearer view.

Docker and Gazebo are listed in the original project record. This description summarizes the report's abstract and methodology; it does not claim quantitative accuracy or assign every system module to one individual.

## Research Dissemination

The linked ACPA11 video is a research presentation, rather than a separately identified demonstration-only video. The full report, including its methodology and evaluation sections, is preserved in Resources. Individual contribution boundaries and quantitative results are not inferred from the project summary.
