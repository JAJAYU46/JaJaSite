---
title: "Cinema Reservation System"
description: "Developed a movie booking web application with React and ASP.NET MVC, including CRUD operations, session-based login, seat reservations, and timestamp-based conflict handling for concurrent bookings."
date: "2026-11-08"
dateVerified: false
author: "jaja"
projectCategory: "software"
tags: ["software"]
technologies: ["React", "ASP.NET MVC", "CRUD", "Sessions", "Concurrency Control"]
order: 70
featured: false
showOnHome: true
cover: "https://drive.google.com/thumbnail?id=13qPVCq-X1g7r0voGRkdB6FWfwh88xxwu"
coverAlt: "Source project image for Cinema Reservation System"
youtubeUrl: "https://youtu.be/FpBPMXGWN6Q"
youtubeLabel: "Project demonstration"
resources: [{"label": "Reservation System Demonstration", "url": "https://youtu.be/FpBPMXGWN6Q"}, {"label": "Original Project Image (Google Drive)", "url": "https://drive.google.com/thumbnail?id=13qPVCq-X1g7r0voGRkdB6FWfwh88xxwu"}]
---

<!-- Source: MyWeb.xlsx / MyProject rows 13. Markdown is the canonical published content. -->

## Overview

This web application supports cinema booking, including selecting seats and managing users, screenings, and reservations. It addresses the conflict that can occur when multiple users try to reserve the same seat.

## Implementation

The frontend uses React, and the backend follows an ASP.NET MVC architecture. CRUD operations manage user, screening, and booking data. Session-based state supports user login, while a timestamp-based concurrency mechanism handles conflicting seat reservations.

The source describes the conflict-handling approach but does not specify its transaction isolation level or provide load-test results. The demonstration video is preserved in Resources.

## Technologies

React, ASP.NET MVC, CRUD operations, sessions, and timestamp-based concurrency control. React belongs to this original project; the portfolio itself remains Astro-based.
