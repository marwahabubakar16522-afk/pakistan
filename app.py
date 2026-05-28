from flask import Flask, render_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dr. Abu Bakar Hafeez Bhatti - Liver Transplant Surgeon</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary-color: #1e3c72;
            --secondary-color: #2a5298;
            --accent-color: #f39c12;
            --text-dark: #2c3e50;
            --text-light: #ecf0f1;
            --border-color: #ecf0f1;
            --shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-dark);
            background-color: #f8f9fa;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Navigation */
        .navbar {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: var(--shadow);
        }

        .navbar .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--accent-color);
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            transition: color 0.3s ease;
            font-weight: 500;
        }

        .nav-links a:hover {
            color: var(--accent-color);
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 80px 20px;
            text-align: center;
            min-height: 600px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .hero-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            align-items: center;
            max-width: 1000px;
        }

        .hero-text-content h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            font-weight: 700;
        }

        .subtitle {
            font-size: 1.8rem;
            margin-bottom: 1rem;
            color: var(--accent-color);
            font-weight: 600;
        }

        .hero-text {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            color: #ecf0f1;
        }

        .cta-button {
            display: inline-block;
            background-color: var(--accent-color);
            color: var(--text-dark);
            padding: 12px 30px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: var(--shadow);
            margin-right: 1rem;
        }

        .cta-button:hover {
            background-color: #e67e22;
            transform: translateY(-3px);
            box-shadow: 0 5px 20px rgba(243, 156, 18, 0.3);
        }

        .hero-image {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .hero-image img {
            width: 100%;
            max-width: 350px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease;
        }

        .hero-image img:hover {
            transform: scale(1.05);
        }

        /* About Section */
        .about {
            padding: 80px 20px;
            background-color: white;
        }

        .about h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: var(--primary-color);
        }

        .about-content {
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.8;
            font-size: 1.1rem;
        }

        .about-content p {
            margin-bottom: 1.5rem;
            text-align: justify;
        }

        /* Qualifications Section */
        .qualifications {
            padding: 80px 20px;
            background-color: #f8f9fa;
        }

        .qualifications h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: var(--primary-color);
        }

        .qualifications-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .qual-card {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: var(--shadow);
            text-align: center;
            transition: all 0.3s ease;
            border-top: 4px solid var(--accent-color);
        }

        .qual-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 25px rgba(0, 0, 0, 0.15);
        }

        .qual-card h3 {
            color: var(--primary-color);
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }

        .qual-card p {
            font-size: 1rem;
            color: var(--text-dark);
            margin-bottom: 0.5rem;
        }

        .qual-card .detail {
            color: #7f8c8d;
            font-size: 0.95rem;
            font-style: italic;
        }

        /* Experience Section */
        .experience {
            padding: 80px 20px;
            background-color: white;
        }

        .experience h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: var(--primary-color);
        }

        .experience-content {
            max-width: 900px;
            margin: 0 auto;
        }

        .exp-item {
            margin-bottom: 2.5rem;
            padding: 2rem;
            border-left: 4px solid var(--accent-color);
            background-color: #f8f9fa;
            border-radius: 5px;
        }

        .exp-item h3 {
            color: var(--primary-color);
            margin-bottom: 0.8rem;
            font-size: 1.3rem;
        }

        .exp-item p {
            margin-bottom: 0.5rem;
            line-height: 1.6;
        }

        .exp-item .detail {
            color: #7f8c8d;
            font-size: 0.95rem;
        }

        .expertise-list {
            list-style: none;
            margin-top: 1rem;
        }

        .expertise-list li {
            padding: 0.5rem 0;
            padding-left: 1.5rem;
            position: relative;
        }

        .expertise-list li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--accent-color);
            font-weight: bold;
        }

        /* Research Section */
        .research {
            padding: 80px 20px;
            background-color: #f8f9fa;
        }

        .research h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: var(--primary-color);
        }

        .research-content {
            max-width: 900px;
            margin: 0 auto;
        }

        .research-item {
            background: white;
            padding: 2rem;
            margin-bottom: 2rem;
            border-radius: 8px;
            box-shadow: var(--shadow);
            border-left: 4px solid var(--accent-color);
        }

        .research-item h3 {
            color: var(--primary-color);
            margin-bottom: 1rem;
        }

        .research-item p {
            margin-bottom: 0.8rem;
            line-height: 1.6;
        }

        .research-highlight {
            background-color: #e8f4f8;
            padding: 1.5rem;
            border-radius: 5px;
            margin-top: 1rem;
        }

        .research-highlight strong {
            color: var(--primary-color);
        }

        /* Contact Section */
        .contact {
            padding: 80px 20px;
            background-color: white;
        }

        .contact h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: var(--primary-color);
        }

        .contact-content {
            max-width: 1000px;
            margin: 0 auto;
        }

        .contact-info {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .contact-item {
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: var(--shadow);
        }

        .contact-item h3 {
            color: var(--primary-color);
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }

        .contact-item p {
            margin-bottom: 0.5rem;
            line-height: 1.6;
        }

        .contact-item .detail {
            color: #7f8c8d;
            font-size: 0.95rem;
        }

        .profile-links {
            list-style: none;
            margin-top: 1rem;
        }

        .profile-links li {
            margin-bottom: 0.8rem;
        }

        .profile-links a {
            color: var(--secondary-color);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        .profile-links a:hover {
            color: var(--accent-color);
        }

        /* Footer */
        .footer {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 2rem 20px;
            text-align: center;
        }

        .footer p {
            margin-bottom: 0.5rem;
        }

        .footer-text {
            font-size: 0.9rem;
            color: #ecf0f1;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-links {
                gap: 1rem;
                font-size: 0.9rem;
            }

            .hero-content {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .hero-text-content h1 {
                font-size: 2rem;
            }

            .subtitle {
                font-size: 1.3rem;
            }

            .about h2,
            .qualifications h2,
            .experience h2,
            .research h2,
            .contact h2 {
                font-size: 2rem;
            }

            .qualifications-grid {
                grid-template-columns: 1fr;
            }

            .contact-info {
                grid-template-columns: 1fr;
            }

            .hero-image img {
                max-width: 280px;
            }
        }

        @media (max-width: 480px) {
            .nav-links {
                gap: 0.5rem;
                font-size: 0.8rem;
            }

            .hero-text-content h1 {
                font-size: 1.5rem;
            }

            .subtitle {
                font-size: 1rem;
            }

            .cta-button {
                padding: 10px 20px;
                font-size: 0.95rem;
                margin-right: 0.5rem;
                display: block;
                margin-bottom: 0.5rem;
            }

            .hero-image img {
                max-width: 220px;
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="logo">Dr. Abu Bakar Hafeez Bhatti</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#qualifications">Qualifications</a></li>
                <li><a href="#experience">Experience</a></li>
                <li><a href="#research">Research</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Home Section -->
    <section id="home" class="hero">
        <div class="hero-content">
            <div class="hero-text-content">
                <h1>Dr. Abu Bakar Hafeez Bhatti</h1>
                <p class="subtitle">Consultant Liver Transplant & Hepatobiliary Surgeon</p>
                <p class="hero-text">Director of Transplant Program at Shifa International Hospital</p>
                <p class="hero-text">Prolific Researcher with 75+ International Publications</p>
                <div>
                    <a href="#research" class="cta-button">View Research</a>
                    <a href="#contact" class="cta-button">Get in Touch</a>
                </div>
            </div>
            <div class="hero-image">
                <img src="https://media.licdn.com/dms/image/v2/C4D03AQG_sY_dFe_eXg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1542276873206?e=2147483647&v=beta&t=abc123" alt="Dr. Abu Bakar Hafeez Bhatti" onerror="this.style.display='none'">
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2>About Dr. Abu Bakar Hafeez Bhatti</h2>
            <div class="about-content">
                <p>
                    Dr. Abu Bakar Hafeez Bhatti is a highly regarded Consultant Liver Transplant and Hepato-Pancreatico-Biliary (HPB) Surgeon 
                    and the Director of the Transplant Program at Shifa International Hospital in Islamabad, Pakistan. With extensive training 
                    from international institutions and decades of experience, he is a leading figure in advancing liver transplant programs in Pakistan.
                </p>
                <p>
                    As a prolific researcher with over 75 international publications in hepatobiliary surgery and oncology, Dr. Bhatti is an 
                    active contributor to the global understanding of liver surgery and transplantation, particularly within the context of South Asia. 
                    He is dedicated to providing world-class surgical care and advancing the field of hepatobiliary medicine through clinical excellence 
                    and groundbreaking research.
                </p>
            </div>
        </div>
    </section>

    <!-- Qualifications Section -->
    <section id="qualifications" class="qualifications">
        <div class="container">
            <h2>Qualifications & Certifications</h2>
            <div class="qualifications-grid">
                <div class="qual-card">
                    <h3>Medical Degree</h3>
                    <p>MBBS</p>
                    <p class="detail">Dow Medical College, Karachi</p>
                </div>
                <div class="qual-card">
                    <h3>Residency</h3>
                    <p>General Surgery</p>
                    <p class="detail">Dow University of Health Sciences, Karachi</p>
                </div>
                <div class="qual-card">
                    <h3>Postgraduate Qualification</h3>
                    <p>FCPS</p>
                    <p class="detail">Fellow of College of Physicians & Surgeons, Pakistan</p>
                </div>
                <div class="qual-card">
                    <h3>International Fellowship</h3>
                    <p>FRCS (Glasgow)</p>
                    <p class="detail">Fellow of the Royal College of Surgeons, Glasgow, UK</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience Section -->
    <section id="experience" class="experience">
        <div class="container">
            <h2>Professional Experience</h2>
            <div class="experience-content">
                <div class="exp-item">
                    <h3>Current Position</h3>
                    <p><strong>Director of Transplant Program</strong></p>
                    <p><strong>Consultant Liver Transplantation & Hepatobiliary Pancreatic Surgery</strong></p>
                    <p class="detail">Shifa International Hospital, Islamabad</p>
                </div>
                <div class="exp-item">
                    <h3>Areas of Expertise</h3>
                    <ul class="expertise-list">
                        <li>Liver Transplant Surgery (LDLT & DDLT)</li>
                        <li>Hepato-Pancreato-Biliary Surgery</li>
                        <li>Surgical Oncology</li>
                        <li>Complex Abdominal Surgery</li>
                        <li>Living Donor Liver Transplantation for HCC</li>
                    </ul>
                </div>
                <div class="exp-item">
                    <h3>Professional Recognition</h3>
                    <p>Extensive experience in performing complex surgical procedures with excellent patient outcomes</p>
                    <p class="detail">Dedicated to advancing surgical excellence and patient care in Pakistan</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Research Section -->
    <section id="research" class="research">
        <div class="container">
            <h2>Research & Publications</h2>
            <div class="research-content">
                <div class="research-item">
                    <h3>Research Overview</h3>
                    <p>
                        Dr. Bhatti is a prolific researcher with over 75 international publications in hepatobiliary surgery and oncology. 
                        His research contributes significantly to the global understanding of liver surgery and transplantation, with a particular 
                        focus on South Asian populations and their unique clinical challenges.
                    </p>
                    <div class="research-highlight">
                        <strong>Key Research Areas:</strong>
                        <ul class="expertise-list">
                            <li>Hepatocellular Carcinoma (HCC) - Efficacy and outcomes of Living Donor Liver Transplantation (LDLT)</li>
                            <li>Liver Donor Assessment - Long-term medical and quality-of-life outcomes for living liver donors</li>
                            <li>Oncological Surgery - Breast conservative therapy and early-onset rectal cancer in Pakistani population</li>
                            <li>Clinical Guidelines - Co-authoring national guidelines for hilar cholangiocarcinoma diagnosis and treatment</li>
                        </ul>
                    </div>
                </div>

                <div class="research-item">
                    <h3>Academic Contributions</h3>
                    <p><strong>Publication Count: 75+ International Publications</strong></p>
                    <p>
                        Dr. Bhatti has published extensively in peer-reviewed journals and presented his research at major international 
                        medical conferences. He is also an active reviewer for numerous international medical journals.
                    </p>
                </div>

                <div class="research-item">
                    <h3>Access His Publications</h3>
                    <p>View Dr. Bhatti's complete bibliography and academic contributions across major scientific databases:</p>
                    <ul class="profile-links">
                        <li><a href="https://www.researchgate.net/profile/Abu-Bhatti-2" target="_blank">ResearchGate Profile</a></li>
                        <li><a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank">PubMed Database</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2>Contact Information</h2>
            <div class="contact-content">
                <div class="contact-info">
                    <div class="contact-item">
                        <h3>Hospital</h3>
                        <p>Shifa International Hospital</p>
                        <p class="detail">H-8/4, Islamabad, Pakistan</p>
                        <p class="detail"><strong>Phone:</strong> 0313 5550131</p>
                    </div>
                    <div class="contact-item">
                        <h3>Appointment Booking</h3>
                        <p>Contact Shifa International Hospital</p>
                        <p class="detail">Visit: www.shifa.com.pk</p>
                        <p class="detail">Call: 0313 5550131 for appointments</p>
                    </div>
                    <div class="contact-item">
                        <h3>Professional Profiles</h3>
                        <p>Connect & Learn More:</p>
                        <ul class="profile-links">
                            <li><a href="https://www.linkedin.com/in/abu-bakar-hafeez-bhatti-8b34342b1/" target="_blank">LinkedIn Profile</a></li>
                            <li><a href="https://www.researchgate.net/profile/Abu-Bhatti-2" target="_blank">ResearchGate Profile</a></li>
                            <li><a href="https://www.shifa.com.pk" target="_blank">Shifa International Hospital</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2026 Dr. Abu Bakar Hafeez Bhatti. All rights reserved.</p>
            <p class="footer-text">Professional website dedicated to showcasing medical expertise and academic achievements.</p>
        </div>
    </footer>

    <script>
        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Add animation to elements on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Observe all sections and cards
        document.querySelectorAll('.about, .qualifications, .experience, .research, .contact, .qual-card, .exp-item, .contact-item, .research-item').forEach(el => {
            observer.observe(el);
        });

        console.log('Website loaded successfully!');
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_string(html_content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
