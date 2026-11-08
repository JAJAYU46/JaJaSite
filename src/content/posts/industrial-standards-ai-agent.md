---
title: "Industrial Standards AI Agent"
description: "Prototyped an industrial-standards question-answering tool using vectorized reference documents and retrieval-augmented generation, with a user-facing interface."
date: "2026-11-08"
dateVerified: false
author: "jaja"
projectCategory: "software"
tags: ["software"]
technologies: ["RAG", "Vector Database", "AI Agent", "Gradio"]
order: 100
featured: false
showOnHome: false
cover: "https://drive.google.com/thumbnail?id=1a1MB7NaofM5HRwrkvasniyOb-Rmgqg_3"
coverAlt: "Source project image for Industrial Standards AI Agent"
resources: [{"label": "Prototype Documentation", "url": "https://drive.google.com/file/d/1UCBANRYIlkimmNB1PdLxv-PzzwGbCck9/view?usp=drive_link"}, {"label": "Original Project Image (Google Drive)", "url": "https://drive.google.com/thumbnail?id=1a1MB7NaofM5HRwrkvasniyOb-Rmgqg_3"}, {"label": "Prototype Demonstration (linked in the report)", "url": "https://youtu.be/UfZgKLt_768?si=UbmXFmzrK2Mg4VCF"}, {"label": "Gather Town Exhibition Presentation (linked in the report)", "url": "https://youtu.be/ALsJD0Rnkuc?si=W2TTRqhqdLSPz6jS"}, {"label": "Project Files (linked in the report)", "url": "https://drive.google.com/drive/folders/1mVwZOQpd_-JzKka9I75hcWHPUD8VF2XR?usp=drive_link"}, {"label": "Colab Notebook (linked in the report)", "url": "https://colab.research.google.com/drive/16uX9aaFbItnxTt6MBq_Pn42K9p5DX78u?usp=drive_link"}, {"label": "Original Project Proposal (linked in the report)", "url": "https://drive.google.com/file/d/10f8SDH_P3T2t06zu7ll3zg6KXD_RvlSs/view?usp=drive_link"}]
youtubeUrl: "https://youtu.be/UfZgKLt_768?si=UbmXFmzrK2Mg4VCF"
youtubeLabel: "Prototype demonstration"
---

## Overview

This prototype answers questions about industrial standards using reference knowledge and user-supplied standards documents. It is a project implementation of retrieval-augmented generation (RAG).

## Implementation

Reference files and uploaded standards documents are converted into a vector database. A Gradio interface accepts documents and questions, and retrieved material is passed to an answering agent.

The public project report identifies `sentence-transformers/all-MiniLM-L6-v2` for embeddings and `llama-3.3-70b-versatile` for the agent. Its workflow includes a table-processing stage that reorganizes extracted data into JSON, followed by retrieval of relevant passages and a separate answering stage.

This is a prototype workflow, not a validated standards-compliance decision system. No answer-accuracy, reliability, or advanced AI research claims are made.

## Technologies

Vector databases, retrieval-augmented generation, an AI agent workflow, and Gradio. The report supplies a demonstration, an exhibition presentation, a notebook, project files, and the proposal; their original URLs are preserved in Resources.
