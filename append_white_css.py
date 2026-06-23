white_css = """
/* ================================================
   SOLUTION ANALYTICS GRID (SOLUTION 07)
   ================================================ */
.sol-analytics-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    margin-bottom: 64px;
}

.sol-analytics-card {
    background: #ffffff; /* Light card background */
    border: 1px solid rgba(0, 0, 0, 0.08);
    border-radius: 18px;
    padding: 32px;
    display: flex;
    flex-direction: column;
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.sol-analytics-card:hover {
    transform: translateY(-8px);
    border-color: rgba(200, 16, 46, 0.3);
    box-shadow: 0 24px 64px rgba(0, 0, 0, 0.08);
}

.sac-icon {
    width: 56px;
    height: 56px;
    background: rgba(200, 16, 46, 0.1);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--red);
    margin-bottom: 24px;
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), background 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.sol-analytics-card:hover .sac-icon {
    transform: scale(1.1) rotate(5deg);
    background: rgba(200, 16, 46, 0.15);
}

.sac-title {
    font-family: var(--font-display);
    font-size: 22px;
    font-weight: 700;
    color: var(--dark);
    margin-bottom: 16px;
    line-height: 1.2;
}

.sac-desc {
    font-size: 14.5px;
    color: #4B5563;
    line-height: 1.6;
    margin-bottom: 24px;
}

.sol-analytics-card .sol-feat-list {
    margin-bottom: auto; /* pushes the image down */
    color: #4B5563;
}

/* Why Choose Section */
.sol-why-choose {
    background: #f9fafb;
    border: 1px solid rgba(0, 0, 0, 0.08);
    border-radius: 18px;
    padding: 40px;
}

.sol-why-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
}

.sw-item {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 15px;
    color: #4B5563;
    font-weight: 500;
}

@media (max-width: 1024px) {
    .sol-analytics-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .sol-analytics-grid {
        grid-template-columns: 1fr;
    }
}
"""

with open("index.css", "a", encoding="utf-8") as f:
    f.write(white_css)

print("Appended white theme CSS successfully.")
