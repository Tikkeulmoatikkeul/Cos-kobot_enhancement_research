![header](https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;customColorList=10&amp;height=200&amp;text=Kobot%20v.1.5%20enhancement%20research&amp;fontSize=50&amp;animation=twinkling&amp;fontAlign=68&amp;fontAlignY=36)
![header](https://capsule-render.vercel.app/api?type=rect&theme=speech&text=Hello%20there!&fontAlign=30&fontSize=40&desc=Welcome%20to%20my%20repo&descAlign=65&descAlignY=50&height=120)
<p align="left">
  <!-- 말풍선 본문 -->
  <img src="https://capsule-render.vercel.app/api?type=rect&theme=speech
  &text=Kobot%20v.1.5%20enhancement%20research
  &desc=제%20README에%20오신%20걸%20환영해요
  &fontSize=28
  &fontAlign=30
  &descAlign=60
  &descAlignY=55
  &height=100" />

  <!-- 말풍선 꼬리 -->
  <br/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/TriangleArrow-Down.svg" width="40"/>
</p>



## Overview
Proposed improvements for Kobot, a generative AI service launched by Statistics Korea to promote statistical usage.
This project was conducted as part of the 2025 1st Youth Internship Program, in which five members of the Statistical Service Innovation Task Force participated. The topic is closely related to the interns' main tasks-building and curating training data for Kobot-which served as a strong motivation for team members to take part in this project.

## Timeline
- May 8 (Thu): Kick-off meeting
- June 19 (Thu): Mid-term presentation
- Sept 5 (Fri): Final presentation

## 0. User Insights
- Feedback from internal users
- Hands-on usage
- Survey results

## 1. UI/UX Improvement
- Added features: Monthly popular statistics and related resource reccommendations
- Presented Figma screens for the main page, result page, Term explanation panel, and help & FAQ, including screens for the newly added features
- Modified response format to include key summary, representative figures, and context/purpose of statistics

## 2. Prompt Engineering
- Development of question guides from the user perspective
  - Analysis of responses by question type, including diversified time expressions, comparative/choice questions, and sensitivity to specific keywords
- Creation of prompt templates for question refinement
  - target_augmentation_template
  - time_normalization_template

## 3. Graph search with VDB
- Proposed combining graph traversal techniques with the existing VDB-based RAG system
- Created six nodes based on shared information-Statistics, Tables, Field, Institution, Document, Target
- Developed and applied templates for attribution extraction:
  - survey_classification_template
  - criteria_extraction_template
  - target_extraction_template
  



**Tech Stack**

![Python](https://img.shields.io/badge/Python-F7DF1E?style=flat&logo=python&logoColor=black)
![Figma](https://img.shields.io/badge/Figma-007ACC?style=flat&logo=figma&logoColor=white)
![Clova Studio](https://img.shields.io/badge/Clova_Studio-00C73C?style=flat&logo=Naver&logoColor=white)
