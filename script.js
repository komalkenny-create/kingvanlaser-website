// Product Details Data
const products = {
    1: {
        name: 'Single Side, Single Traction Automatic Marking Machine',
        desc: 'Economical automatic marking equipment for single-side marking needs',
        features: [
            'Single-side laser marking, clear and permanent',
            'Single traction stable feeding system',
            'High automation, easy to operate',
            'Cost-effective for small to medium production',
            'Suitable for various thermal strip materials'
        ],
        specs: {
            'Marking Type': 'Single-side',
            'Traction System': 'Single traction',
            'Marking Speed': 'Adjustable',
            'Applicable Materials': 'Thermal strips, sealing strips, etc.',
            'Power Supply': '220V/50Hz'
        }
    },
    2: {
        name: 'Single Side, Double Traction Automatic Marking Machine',
        desc: 'Dual traction design for more stable feeding, ideal for longer strips',
        features: [
            'Single-side laser marking with higher precision',
            'Dual traction synchronous feeding for enhanced stability',
            'Suitable for longer thermal strip processing',
            'Smooth operation, reduces material deformation',
            'Significantly improved production efficiency'
        ],
        specs: {
            'Marking Type': 'Single-side',
            'Traction System': 'Double traction',
            'Marking Speed': 'Adjustable',
            'Applicable Materials': 'Thermal strips, sealing strips, etc.',
            'Power Supply': '220V/50Hz'
        }
    },
    3: {
        name: 'Double Side, Single Traction Automatic Marking Machine',
        desc: 'Simultaneous double-side marking with single traction, excellent value',
        features: [
            'Simultaneous double-side laser marking',
            'Single traction feeding system',
            'Complete double-side marking in one pass',
            'High cost performance, widely applicable',
            'Suitable for large-scale production needs'
        ],
        specs: {
            'Marking Type': 'Double-side',
            'Traction System': 'Single traction',
            'Marking Speed': 'Adjustable',
            'Applicable Materials': 'Thermal strips, sealing strips, etc.',
            'Power Supply': '220V/50Hz'
        }
    },
    4: {
        name: 'Double Side, Double Traction Automatic Marking Machine',
        desc: 'Flagship configuration: dual-side marking + dual traction for maximum efficiency',
        features: [
            'Simultaneous double-side laser marking, doubled efficiency',
            'Dual traction precision feeding, ultimate stability',
            'Flagship configuration with premium performance',
            'Maximum production efficiency for large-scale manufacturing',
            'Intelligent control system, user-friendly operation'
        ],
        specs: {
            'Marking Type': 'Double-side',
            'Traction System': 'Double traction',
            'Marking Speed': 'High-speed adjustable',
            'Applicable Materials': 'Thermal strips, sealing strips, etc.',
            'Power Supply': '220V/50Hz'
        }
    }
};

// Search Data
const searchData = [
    { type: 'benefit', title: 'Compliance & Certification', desc: 'CE, ISO 9001, AAMA, GB/T requirements', link: '#benefits' },
    { type: 'benefit', title: 'Product Traceability', desc: 'Quality control and recall management', link: '#benefits' },
    { type: 'benefit', title: 'Brand & Anti-Counterfeiting', desc: '15-30% higher prices with branding', link: '#benefits' },
    { type: 'benefit', title: 'Customer Trust', desc: 'Factory audit requirements', link: '#benefits' },
    { type: 'product', title: 'Single Side, Single Traction', desc: 'Economical model for single-side marking', link: '#products' },
    { type: 'product', title: 'Single Side, Double Traction', desc: 'Dual traction for stable feeding', link: '#products' },
    { type: 'product', title: 'Double Side, Single Traction', desc: 'Simultaneous double-side marking', link: '#products' },
    { type: 'product', title: 'Double Side, Double Traction', desc: 'Flagship configuration for maximum efficiency', link: '#products' },
    { type: 'blog', title: 'Understanding Laser Marking Technology', desc: 'A comprehensive guide to laser marking', link: '#blog' },
    { type: 'blog', title: 'How to Choose the Right Marking Machine', desc: 'Key factors to consider when selecting', link: '#blog' },
    { type: 'blog', title: '5 Maintenance Tips', desc: 'Extend your machine lifespan', link: '#blog' },
    { type: 'news', title: 'International Manufacturing Expo 2026', desc: 'Latest exhibition news', link: '#news' },
    { type: 'news', title: 'European Distribution Partnership', desc: 'Expanding global reach', link: '#news' },
    { type: 'page', title: 'Products', desc: 'View all our marking machines', link: '#products' },
    { type: 'page', title: 'Blog', desc: 'Latest articles and guides', link: '#blog' },
    { type: 'page', title: 'News', desc: 'Company news and updates', link: '#news' },
    { type: 'page', title: 'Contact', desc: 'Get in touch with us', link: '#contact' }
];

// Show Product Detail Modal
function showProductDetail(productId) {
    const product = products[productId];
    if (!product) return;
    const modal = document.getElementById('productModal');
    const modalBody = document.getElementById('modalBody');
    let specsHtml = '';
    for (const [key, value] of Object.entries(product.specs)) {
        specsHtml += `<li><strong>${key}:</strong> ${value}</li>`;
    }
    modalBody.innerHTML = `
        <h3>${product.name}</h3>
        <p>${product.desc}</p>
        <h4 style="margin-top: 20px; margin-bottom: 10px; color: var(--secondary);">Key Features</h4>
        <ul>${product.features.map(f => `<li>${f}</li>`).join('')}</ul>
        <h4 style="margin-top: 20px; margin-bottom: 10px; color: var(--secondary);">Specifications</h4>
        <ul>${specsHtml}</ul>
        <a href="#contact" class="btn btn-primary" onclick="closeProductModal()" style="display: inline-block; margin-top: 20px;">Request a Quote</a>
    `;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeProductModal() {
    document.getElementById('productModal').classList.remove('active');
    document.body.style.overflow = '';
}

document.getElementById('productModal').addEventListener('click', function(e) {
    if (e.target === this) closeProductModal();
});

// Sign In / Sign Up Functions
function openSignIn() {
    document.getElementById('signInModal').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeSignInModal() {
    document.getElementById('signInModal').classList.remove('active');
    document.body.style.overflow = '';
}

function openSignUp() {
    document.getElementById('signUpModal').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeSignUpModal() {
    document.getElementById('signUpModal').classList.remove('active');
    document.body.style.overflow = '';
}

function switchToSignUp() {
    closeSignInModal();
    setTimeout(openSignUp, 200);
}

function switchToSignIn() {
    closeSignUpModal();
    setTimeout(openSignIn, 200);
}

document.getElementById('signInModal').addEventListener('click', function(e) {
    if (e.target === this) closeSignInModal();
});

document.getElementById('signUpModal').addEventListener('click', function(e) {
    if (e.target === this) closeSignUpModal();
});

document.getElementById('signInBtn').addEventListener('click', openSignIn);
document.getElementById('signUpBtn').addEventListener('click', openSignUp);

// Form Submissions
document.getElementById('signInForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Sign in functionality would connect to backend authentication system.');
    closeSignInModal();
});

document.getElementById('signUpForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Account created successfully! Welcome to LaserMark Pro.');
    closeSignUpModal();
});

document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const form = this;
    const data = new FormData(form);
    
    // 👇 请在这里替换为你自己的 Formspree ID
    // 获取方式：注册 https://formspree.io/ -> 创建 Form -> 复制 Endpoint ID (例如: xrg...)
    const FORMSPREE_ID = 'YOUR_FORMSPREE_ID'; 
    
    if (FORMSPREE_ID === 'YOUR_FORMSPREE_ID') {
        alert('演示模式：请在 script.js 中配置你的 Formspree ID 以接收真实邮件。');
        form.reset();
        return;
    }

    fetch(`https://formspree.io/f/${FORMSPREE_ID}`, {
        method: 'POST',
        body: data,
        headers: { 'Accept': 'application/json' }
    }).then(response => {
        if (response.ok) {
            alert('Thank you for your inquiry! We will contact you shortly.');
            form.reset();
        } else {
            response.json().then(data => {
                if (Object.hasOwn(data, 'errors')) {
                    alert(data["errors"].map(error => error["message"]).join(", "));
                } else {
                    alert('Oops! There was a problem submitting your form');
                }
            })
        }
    }).catch(error => {
        alert('Oops! There was a problem submitting your form');
    });
});

// Search Functionality
const searchInput = document.getElementById('searchInput');
const searchBtn = document.getElementById('searchBtn');
const searchResults = document.getElementById('searchResults');

function performSearch(query) {
    if (!query.trim()) {
        searchResults.classList.remove('active');
        return;
    }
    
    const filtered = searchData.filter(item => 
        item.title.toLowerCase().includes(query.toLowerCase()) ||
        item.desc.toLowerCase().includes(query.toLowerCase())
    );
    
    if (filtered.length === 0) {
        searchResults.innerHTML = '<div class="search-result-item"><p>No results found</p></div>';
    } else {
        searchResults.innerHTML = filtered.map(item => `
            <div class="search-result-item" onclick="window.location.href='${item.link}'">
                <h4>${item.title}</h4>
                <p>${item.desc}</p>
            </div>
        `).join('');
    }
    
    searchResults.classList.add('active');
}

searchInput.addEventListener('input', function() {
    performSearch(this.value);
});

searchBtn.addEventListener('click', function() {
    performSearch(searchInput.value);
});

searchInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        performSearch(this.value);
    }
});

document.addEventListener('click', function(e) {
    if (!e.target.closest('.search-bar')) {
        searchResults.classList.remove('active');
    }
});

// ESC key to close modals
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeProductModal();
        closeSignInModal();
        closeSignUpModal();
    }
});

// Mobile Menu Toggle
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const navLinks = document.querySelector('.nav-links');

if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', function() {
        navLinks.classList.toggle('active');
        this.classList.toggle('active');
    });
}

document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', function() {
        navLinks.classList.remove('active');
        mobileMenuBtn.classList.remove('active');
    });
});

// Video Player
const videoOverlay = document.getElementById('videoOverlay');
const demoVideo = document.getElementById('demoVideo');

if (videoOverlay && demoVideo) {
    videoOverlay.addEventListener('click', function() {
        if (demoVideo.paused) {
            demoVideo.play();
            videoOverlay.classList.add('hidden');
        }
    });

    demoVideo.addEventListener('click', function() {
        if (!demoVideo.paused) {
            demoVideo.pause();
            videoOverlay.classList.remove('hidden');
        }
    });

    demoVideo.addEventListener('ended', function() {
        videoOverlay.classList.remove('hidden');
    });
}

// Scroll Animations
const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -40px 0px' };
const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.addEventListener('DOMContentLoaded', function() {
    const animatedElements = document.querySelectorAll('.product-card, .feature-card, .blog-card, .news-item, .gallery-item');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(el);
    });
});

// Number Animation
function animateNumber(element, target, duration = 1500) {
    const increment = target / (duration / 16);
    let current = 0;
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current) + (element.dataset.suffix || '');
    }, 16);
}

const statsObserver = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.querySelectorAll('.stat-number, .stat-num').forEach(stat => {
                const number = parseInt(stat.textContent);
                const suffix = stat.textContent.replace(/[0-9]/g, '');
                if (!isNaN(number) && !stat.dataset.animated) {
                    stat.dataset.animated = 'true';
                    stat.dataset.suffix = suffix;
                    animateNumber(stat, number);
                }
            });
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('.hero-stats, .about-stats').forEach(section => {
    statsObserver.observe(section);
});

console.log('LaserMark Pro website loaded 🚀');

// ===== Lightbox Functionality =====
const lightbox = document.getElementById('lightbox');
const lightboxClose = document.getElementById('lightboxClose');
const lightboxContent = document.getElementById('lightboxContent');
const lightboxCaption = document.getElementById('lightboxCaption');

if (lightbox) {
    // Open lightbox on gallery item click
    document.querySelectorAll('.gallery-item').forEach(item => {
        item.addEventListener('click', function() {
            const img = this.querySelector('.gallery-img');
            const caption = this.querySelector('h4')?.textContent || 'Gallery Image';
            
            // Clone the gallery image content
            lightboxContent.innerHTML = '';
            const clonedImg = img.cloneNode(true);
            clonedImg.style.width = '100%';
            clonedImg.style.height = 'auto';
            clonedImg.style.maxHeight = '80vh';
            lightboxContent.appendChild(clonedImg);
            
            lightboxCaption.textContent = caption;
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });

    // Close lightbox
    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }

    if (lightboxClose) {
        lightboxClose.addEventListener('click', closeLightbox);
    }

    lightbox.addEventListener('click', function(e) {
        if (e.target === this) {
            closeLightbox();
        }
    });

    // ESC key to close lightbox
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
            closeLightbox();
        }
    });
}

// ===== Enhanced Navigation Scroll Effect =====
const navbar = document.querySelector('.navbar');
let lastScroll = 0;

if (navbar) {
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        } else {
            navbar.style.boxShadow = 'var(--shadow)';
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        }
        
        lastScroll = currentScroll;
    });
}

// ===== Enhanced Form Interactions =====
document.querySelectorAll('.contact-form input, .contact-form textarea, .contact-form select').forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.style.transform = 'scale(1.02)';
        this.parentElement.style.transition = 'transform 0.3s ease';
    });
    
    input.addEventListener('blur', function() {
        this.parentElement.style.transform = 'scale(1)';
    });
});

// ===== Smooth Scroll for Anchor Links =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href.length > 1) {
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const offsetTop = target.offsetTop - 80;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        }
    });
});

// ===== Button Click Effects =====
document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        // Create ripple effect
        const ripple = document.createElement('span');
        ripple.style.position = 'absolute';
        ripple.style.width = '20px';
        ripple.style.height = '20px';
        ripple.style.background = 'rgba(255, 255, 255, 0.6)';
        ripple.style.borderRadius = '50%';
        ripple.style.transform = 'scale(0)';
        ripple.style.animation = 'ripple 0.6s linear';
        ripple.style.left = e.offsetX + 'px';
        ripple.style.top = e.offsetY + 'px';
        ripple.style.pointerEvents = 'none';
        
        this.style.position = 'relative';
        this.style.overflow = 'hidden';
        this.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    });
});

// Add ripple animation CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// ===== Loading Animation =====
window.addEventListener('load', function() {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 50);
});

// ===== Scroll Animations =====
function initScrollAnimations() {
    // Add fade-in class to sections
    const sections = document.querySelectorAll('.benefit-card, .product-card, .feature-card, .gallery-item, .about-content, .contact-content, .blog-card, .news-item');
    sections.forEach(section => {
        section.classList.add('fade-in');
    });

    // Add slide-in classes
    const aboutText = document.querySelector('.about-text');
    if (aboutText) {
        aboutText.classList.add('slide-in-left');
    }
    
    const aboutImage = document.querySelector('.about-image');
    if (aboutImage) {
        aboutImage.classList.add('slide-in-right');
    }

    const contactInfo = document.querySelector('.contact-info');
    if (contactInfo) {
        contactInfo.classList.add('slide-in-left');
    }

    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.classList.add('slide-in-right');
    }

    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Observe all animated elements
    document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right, .scale-in').forEach(el => {
        scrollObserver.observe(el);
    });
}

// Initialize scroll animations when DOM is ready
document.addEventListener('DOMContentLoaded', initScrollAnimations);

// ===== Enhanced Scroll Animation for Existing Code =====
// Update the existing DOMContentLoaded listener
const originalDOMContentLoaded = document.addEventListener;
document.addEventListener('DOMContentLoaded', function() {
    // Re-observe animated elements with the original observer
    const animatedElements = document.querySelectorAll('.product-card, .feature-card, .blog-card, .news-item, .gallery-item');
    animatedElements.forEach(el => {
        el.style.opacity = '';
        el.style.transform = '';
        el.style.transition = '';
    });
});
