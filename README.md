# Urban-Carbon-Forecast-Strategic-Policy-Optimizer
By integrating SUMO simulation with AWS cloud infrastructure, I have architected a system that doesn't just monitor traffic it predicts and optimizes it. This project showcases my ability to manage complex ETL/ELT processes and translate technical telemetry into transparent, interpretable findings for non-technical stakeholders

Urban-Flow AI: A Digital Twin for Predictive Mobility & Carbon OptimizationProject

Overview:
This project, developed as part of a Master of Data Science curriculum, is a comprehensive Cyber-Physical Intelligence Pipeline designed to bridge the "Intelligence-Action Gap" in smart city governance. It utilizes a high-fidelity digital twin to model urban traffic events, applies AI-driven interventions to mitigate congestion, and processes the resulting data for long-term climate policy optimization.The system functions as a closed-loop intelligence engine: sensing real-time traffic conditions via SUMO, acting to resolve bottlenecks through Dynamic Rerouting, and uploading performance telemetry to AWS S3 for cross-regional stakeholder analysis.

🎯 Core Objectives
This repository addresses four critical challenges in modern urban planning
Predictive Accuracy: Classifying congestion levels in real-time to move from "Reactive" to "Proactive" governance.
Mitigation Impact: Reducing system delays and idling-related emissions through automated rerouting.
Strategic Allocation: Mathematically optimizing municipal budgets to achieve maximum $CO_2$ reduction.
Cloud Scalability: Harmonizing local traffic telemetry into a global data warehouse for policy comparison.

Technical Architecture 1. Data Ingestion & Engineering
(Stage I)Historical Harmonization: Modeled and harmonized 63 years of multi-national emission datasets (1960–2023).
Automated Pipeline: Built a multivariate data pipeline via global APIs, reducing ingestion latency by 30%.
Regional Scope: Dynamically generates datasets for over 15 European territories, including a high-resolution Berlin dataset.

2. Predictive & Optimization Engine
 (Stages II & III)Forecasting: Developed ML-driven algorithms for urban carbon trends, providing a 4.38 Tons $CO_2$/Capita baseline forecast.Digital Twin Simulation: Employs SUMO (Simulation of Urban MObility) to create a digital replica of city grids.
Dynamic Rerouting: Algorithms detect vehicle speeds < 5 km/h and recalculate paths, reducing system delays by 70%.
Mathematical Solver: Uses PuLP for linear programming to prescribe optimal budget allocations.

3. Cloud-Native Analytics (Stage IV)
Cloud Integration: Integrated with AWS S3 using boto3 for scalable data storage and portability.
Visualization: Connects to Power BI for real-time tracking of KPIs such as vehicle flow, average speed, and congestion levels.

📈 Validated Results
The Stage IV validation confirmed the technical robustness of the pipeline with the following performance metrics:
Throughput: Successfully routed 990 vehicles in high-density scenarios.Network Flow: Maintained an average flow of 122.00 veh/hr.
System Speed: Achieved an average velocity of 11.47 m/s.
Budget Efficiency: Achieved a 100% efficiency increase by allocating €95M to Renewable Energy and €5M to Green Buildings to reach an 88-ton reduction potential.

 Technologies Used
 Languages: Python (Pandas, NumPy, PuLP, Boto3)
 Simulation: SUMO (TraCI API)
 Cloud: AWS S3
 Analytics: Power BIFrameworks: SAI-WEFS MethodologyProject
 
 ContributorsHarsha Bodhe – Master of Data Science CandidateShreyas Sandbhor – Project Partner
