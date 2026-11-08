---
title: "Music-Reactive Lighting System"
description: "Built an Arduino-based music-reactive lighting system that analyzes audio frequency content and adjusts LED brightness and switching patterns across three user-selectable modes."
date: "2026-11-08"
dateVerified: false
author: "jaja"
projectCategory: "embedded"
tags: ["embedded"]
technologies: ["Arduino", "FFT", "Sound Sensor", "Soldering", "LED Control"]
order: 150
featured: false
showOnHome: false
cover: "https://drive.google.com/thumbnail?id=1J3Juk-SBEnuULU0Duuxv34G4z_u0IJSh"
coverAlt: "Source project image for Music-Reactive Lighting System"
resources: [{"label": "Project Documentation", "url": "https://docs.google.com/document/d/1ac-VghLU4rsU2PAV6SmzS6wFQxBruPph0U-tRhLg4Hg/edit?usp=sharing"}, {"label": "Original Project Image (Google Drive)", "url": "https://drive.google.com/thumbnail?id=1J3Juk-SBEnuULU0Duuxv34G4z_u0IJSh"}]
---

<!-- Source: MyWeb.xlsx / MyProject rows 17. Markdown is the canonical published content. -->

## Overview

This Arduino-based lighting project changes LED behavior in response to music. A sound sensor captures audio, and frequency analysis connects the signal to lighting effects.

## Implementation

The Arduino FFT library converts sampled audio amplitude data into frequency information. After noise processing, the system uses that information to control LED brightness and the rate of switching between blue and green lights.

A button selects among three modes:

1. Mixed mode: lower-frequency input selects brightness control, and higher-frequency input selects alternating-light control.
2. Brightness mode: the frequency input controls LED brightness.
3. Alternating-light mode: the frequency input controls how quickly the two lights switch.

Two potentiometers adjust the brightest and dimmest LED operating points to accommodate different songs. The work also includes soldered perfboard circuitry and hardware/enclosure design.

## Technologies

Arduino, FFT, a sound sensor module, soldering, and LED control.
