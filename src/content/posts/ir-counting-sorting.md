---
title: "IR Sensor Counting & Container Positioning Prototype"
description: "Built a sensor-driven counting prototype with an LCD display and additional infrared sensors to detect container position and control when movement should stop or continue."
date: "2026-11-08"
dateVerified: false
author: "jaja"
projectCategory: "embedded"
tags: ["embedded"]
technologies: ["IR Sensors", "Raspberry Pi", "LCD"]
order: 170
featured: false
showOnHome: false
cover: "https://drive.google.com/thumbnail?id=1J95gS0e0o292iM58bk8rfGSMyLUeNhYv"
coverAlt: "Source project image for IR Sensor Counting & Container Positioning Prototype"
resources: [{"label": "Original Project Image (Google Drive)", "url": "https://drive.google.com/thumbnail?id=1J95gS0e0o292iM58bk8rfGSMyLUeNhYv"}]
---

<!-- Source: MyWeb.xlsx / MyProject rows 19. Markdown is the canonical published content. -->

## Overview

This sensor prototype counts passing objects and monitors a container's position. Its documented function is counting and container positioning, rather than object sorting.

## Implementation

Each object that passes the counting infrared sensor increments a count shown on an LCD. Three additional infrared sensors determine the container's position and control whether it continues moving or stops.

Automated feeding and packaging are described as possible future extensions, rather than completed capabilities.

## Technologies

Infrared sensors, Raspberry Pi, and an LCD.
