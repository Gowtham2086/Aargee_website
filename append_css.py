modal_css = """
/* ================================================
   QUOTE MODAL
   ================================================ */
.modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.75);
    backdrop-filter: blur(8px);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.4s var(--ease), visibility 0.4s var(--ease);
    padding: 20px;
}

.modal-overlay.active {
    opacity: 1;
    visibility: visible;
}

.modal-container {
    background: #fff;
    border-radius: 16px;
    width: 100%;
    max-width: 600px;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
    transform: translateY(40px);
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 24px 64px rgba(0,0,0,0.4);
}

.modal-overlay.active .modal-container {
    transform: translateY(0);
}

.modal-header {
    padding: 30px 40px 20px;
    border-bottom: 1px solid #f3f4f6;
    position: relative;
}

.modal-close-btn {
    position: absolute;
    top: 24px;
    right: 30px;
    background: transparent;
    border: none;
    cursor: pointer;
    color: #6b7280;
    transition: color 0.2s;
    padding: 5px;
}

.modal-close-btn:hover {
    color: #C8102E;
}

.modal-title {
    font-family: 'Outfit', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: #111827;
    margin-bottom: 8px;
}

.modal-subtitle {
    font-size: 0.95rem;
    color: #6b7280;
    line-height: 1.6;
    margin: 0;
}

.modal-body {
    padding: 30px 40px;
}

.form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
    position: relative;
}

.form-group.full {
    grid-column: 1 / -1;
}

.form-label {
    font-size: 0.85rem;
    font-weight: 600;
    color: #374151;
}

.form-input, .form-select, .form-textarea {
    width: 100%;
    background: transparent;
    border: none;
    border-bottom: 2px solid #e5e7eb;
    padding: 10px 0;
    font-family: 'Inter', sans-serif;
    font-size: 1rem;
    color: #111827;
    transition: border-color 0.3s;
    outline: none;
}

.form-textarea {
    resize: vertical;
    min-height: 80px;
}

.form-input:focus, .form-select:focus, .form-textarea:focus {
    border-bottom-color: #C8102E;
}

.form-input.error, .form-select.error, .form-textarea.error {
    border-bottom-color: #ef4444;
}

.error-msg {
    position: absolute;
    bottom: -18px;
    right: 0;
    font-size: 0.75rem;
    color: #ef4444;
    opacity: 0;
    transition: opacity 0.2s;
}

.form-group.has-error .error-msg {
    opacity: 1;
}

.modal-footer {
    padding: 24px 40px 30px;
    display: flex;
    justify-content: flex-end;
    gap: 16px;
    border-top: 1px solid #f3f4f6;
    background: #fafafa;
    border-radius: 0 0 16px 16px;
}

.btn-modal-cancel {
    background: transparent;
    border: 2px solid #d1d5db;
    color: #374151;
    padding: 12px 24px;
    border-radius: 6px;
    font-family: 'Outfit', sans-serif;
    font-weight: 600;
    font-size: 0.95rem;
    cursor: pointer;
    transition: all 0.2s;
}

.btn-modal-cancel:hover {
    border-color: #9ca3af;
    color: #111827;
}

.btn-modal-submit {
    background: #C8102E;
    border: 2px solid #C8102E;
    color: #fff;
    padding: 12px 32px;
    border-radius: 6px;
    font-family: 'Outfit', sans-serif;
    font-weight: 600;
    font-size: 0.95rem;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 160px;
}

.btn-modal-submit:hover:not(:disabled) {
    background: #a00d24;
    border-color: #a00d24;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(200, 16, 46, 0.3);
}

.btn-modal-submit:disabled {
    opacity: 0.7;
    cursor: not-allowed;
}

.spinner {
    width: 20px;
    height: 20px;
    border: 3px solid rgba(255,255,255,0.3);
    border-radius: 50%;
    border-top-color: #fff;
    animation: spin 1s ease-in-out infinite;
    display: none;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.btn-modal-submit.loading .spinner {
    display: block;
}

.btn-modal-submit.loading .submit-text {
    display: none;
}

/* Success State */
.modal-success {
    position: absolute;
    inset: 0;
    background: #fff;
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 40px;
    z-index: 20;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.4s, visibility 0.4s;
}

.modal-success.active {
    opacity: 1;
    visibility: visible;
}

.success-icon {
    width: 80px;
    height: 80px;
    background: rgba(34, 197, 94, 0.1);
    color: #22c55e;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 24px;
}

.success-icon svg {
    width: 40px;
    height: 40px;
}

.success-title {
    font-family: 'Outfit', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: #111827;
    margin-bottom: 12px;
}

.success-desc {
    color: #4b5563;
    font-size: 1.05rem;
    line-height: 1.6;
    max-width: 400px;
}

@media(max-width: 600px) {
    .form-grid {
        grid-template-columns: 1fr;
        gap: 20px;
    }
    .modal-header, .modal-body, .modal-footer {
        padding-left: 24px;
        padding-right: 24px;
    }
}
"""

with open("index.css", "a", encoding="utf-8") as f:
    f.write("\n" + modal_css)

print("CSS appended to index.css")
