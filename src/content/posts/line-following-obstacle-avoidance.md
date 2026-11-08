---
title: "Line-Following & Obstacle Avoidance Robot"
description: "Built a two-person competition robot for line following and obstacle avoidance, with sensor-driven motor speed adjustments; the team placed third in the class competition."
date: "2026-11-08"
dateVerified: false
author: "jaja"
projectCategory: "embedded"
tags: ["embedded"]
technologies: ["ATmega328P", "IR Sensors", "Ultrasonic Sensor", "Motor Control"]
order: 160
featured: false
showOnHome: false
cover: "https://drive.google.com/thumbnail?id=10MTOcDhG7GKR0Mp8HKiosz-P6i6Bd9nu"
coverAlt: "Source project image for Line-Following & Obstacle Avoidance Robot"
resources: [{"label": "Original Project Image (Google Drive)", "url": "https://drive.google.com/thumbnail?id=10MTOcDhG7GKR0Mp8HKiosz-P6i6Bd9nu"}]
---

<!-- Source: MyWeb.xlsx / MyProject rows 25. Markdown is the canonical published content. -->

## Overview

A two-person team built a robot for a freshman microcontroller course competition. The goal was to complete both a line-following course and an obstacle-avoidance course as quickly as possible.

## Implementation

Three infrared sensors send track-state readings to an ATmega328P microcontroller. Five documented sensor states—110, 100, 000, 001, and 011—select motor-speed adjustments to guide the robot along the line. Sensor-based obstacle avoidance helps the robot keep to the right and avoid obstacles; an ultrasonic sensor is included in the original technology list.

## Results

The two-person team placed third in the class competition, according to the original project record. No lap-time or reliability measurements were supplied.

## Technologies

ATmega328P, infrared sensors, an ultrasonic sensor, and motor control.
