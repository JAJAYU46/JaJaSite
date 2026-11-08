---
title: "Robotic Arm Block Stacking"
description: "Programmed a robot arm to detect blocks from camera input, align its grasp orientation, pick up blocks, and stack them."
date: "2026-11-08"
dateVerified: false
author: "jaja"
projectCategory: "robotics"
tags: ["robotics"]
technologies: ["Robot Arm Control", "Depth Camera", "Image Processing", "Python", "OpenCV"]
order: 50
featured: false
showOnHome: true
cover: "https://drive.google.com/thumbnail?id=1Dv1S7uv-TdjwtX78FQYBj2Dd3K90pP8Z"
coverAlt: "Source project image for Robotic Arm Block Stacking"
youtubeUrl: "https://youtu.be/6URSk8AAQL0?si=6KHBcef8ERqBiobd"
youtubeLabel: "Project demonstration"
resources: [{"label": "Block-Stacking Demonstration", "url": "https://youtu.be/6URSk8AAQL0?si=6KHBcef8ERqBiobd"}, {"label": "Project Documentation", "url": "https://drive.google.com/file/d/1PDHNC-LprKW0frabGmJ4Pirf39SuaQLV/view?usp=drive_link"}, {"label": "Original Project Image (Google Drive)", "url": "https://drive.google.com/thumbnail?id=1Dv1S7uv-TdjwtX78FQYBj2Dd3K90pP8Z"}]
---

<!-- Source: MyWeb.xlsx / MyProject rows 10. Markdown is the canonical published content. -->

## Overview

This manipulation project connects camera-based block recognition with a robot arm's grasping and stacking motions.

## Implementation

The program processes camera input, rotates the arm to align the grasp with a block, picks up the block, and stacks it. The public report documents OpenCV contour extraction, rotated bounding rectangles, and block-centroid/orientation estimation.

Camera images arrive through a robot-arm image topic. A ruler-based calibration maps image coordinates into camera and robot-base coordinates for a fixed-height grasp. Arm commands then move, grasp, lift, and place the blocks.

The report discusses grasp-angle errors and centroid shifts caused by visible block side faces. The source record lists a depth camera; the report excerpt specifically describes a calibrated image-coordinate workflow, not a full 3D reconstruction pipeline. The demonstration and report are linked in Resources.

## Technologies

Robot arm control, a depth camera, Python, OpenCV, and image processing. No arm model or middleware version is inferred from the report excerpt.
