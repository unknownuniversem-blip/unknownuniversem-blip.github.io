(function() {
  if (document.getElementById('hub-network-drawer')) return;

  // Insert Floating Drawer CSS
  const style = document.createElement('style');
  style.innerHTML = `
    #hub-badge {
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: #0284c7;
      color: white;
      padding: 10px 16px;
      border-radius: 99px;
      font-size: 13px;
      font-weight: 700;
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
      cursor: pointer;
      z-index: 999999;
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: system-ui, sans-serif;
    }
    #hub-badge:hover { background: #0369a1; }
    #hub-modal {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.6);
      z-index: 1000000;
      align-items: center;
      justify-content: center;
      font-family: system-ui, sans-serif;
    }
    #hub-modal-content {
      background: #0f172a;
      color: #f8fafc;
      width: 90%;
      max-width: 500px;
      max-height: 80vh;
      border-radius: 12px;
      padding: 20px;
      overflow-y: auto;
      border: 1px solid #334155;
    }
    .hub-link {
      display: block;
      padding: 10px 12px;
      margin-bottom: 8px;
      background: #1e293b;
      border-radius: 6px;
      color: #38bdf8;
      text-decoration: none;
      font-size: 14px;
      font-weight: 600;
    }
    .hub-link:hover { background: #334155; color: white; }
  `;
  document.head.appendChild(style);

  // Insert Floating Badge
  const badge = document.createElement('div');
  badge.id = 'hub-badge';
  badge.innerHTML = '⚡ 20+ Free Tools';
  document.body.appendChild(badge);

  // Insert Modal Grid
  const modal = document.createElement('div');
  modal.id = 'hub-modal';
  modal.innerHTML = `
    <div id="hub-modal-content">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
        <h3 style="margin:0; font-size:16px;">More Free Web Utilities</h3>
        <span id="hub-close" style="cursor:pointer; font-size:20px;">&times;</span>
      </div>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/exam-resizer/">📷 Exam Photo & Signature Resizer</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/sarkari-alert-ai/">📢 Sarkari Alert AI</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/krutidev-unicode-converter/">⌨️ Krutidev to Unicode Converter</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/hindi-typing-tutor/">🇮🇳 Hindi Typing Speed Tutor</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/commerce-accounts-hub/">📚 CBSE Accountancy Solutions</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/pdf-smart-tools/">📄 PDF Compressor & Merger</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/upi-qr-standee/">💳 UPI QR Standee Maker</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/wa-direct/">💬 WhatsApp Direct Chat</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/loan-emi-calculator/">📊 Loan EMI Calculator</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/panchang-choghadiya/">🕉️ Panchang & Choghadiya</a>
    </div>
  `;
  document.body.appendChild(modal);

  badge.onclick = () => modal.style.display = 'flex';
  document.getElementById('hub-close').onclick = () => modal.style.display = 'none';
  modal.onclick = (e) => { if (e.target === modal) modal.style.display = 'none'; };
})();

// Global One-Tap Social Sharing Trigger
window.shareToolToWhatsApp = function() {
  const pageTitle = document.title || "Free Online Tool";
  const pageUrl = window.location.href;
  const message = `Check this free tool: *${pageTitle}* (No ads, works on mobile instantly) 👉 ${pageUrl}`;
  
  if (navigator.share) {
    navigator.share({
      title: pageTitle,
      text: message,
      url: pageUrl
    }).catch(() => {});
  } else {
    window.open("https://api.whatsapp.com/send?text=" + encodeURIComponent(message), "_blank");
  }
};
