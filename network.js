
(function() {
  if (document.getElementById('hub-network-drawer')) return;

  const style = document.createElement('style');
  style.innerHTML = `
    #hub-badge {
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: #0284c7;
      color: white;
      padding: 10px 18px;
      border-radius: 99px;
      font-size: 13px;
      font-weight: 700;
      box-shadow: 0 4px 18px rgba(0,0,0,0.35);
      cursor: pointer;
      z-index: 999999;
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: system-ui, sans-serif;
    }
    #hub-badge:hover { background: #0369a1; transform: scale(1.02); }
    #hub-share-btn {
      position: fixed;
      bottom: 20px;
      left: 20px;
      background: #25D366;
      color: white;
      padding: 10px 16px;
      border-radius: 99px;
      font-size: 13px;
      font-weight: 700;
      box-shadow: 0 4px 18px rgba(0,0,0,0.3);
      cursor: pointer;
      z-index: 999999;
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: system-ui, sans-serif;
      text-decoration: none;
    }
    #hub-share-btn:hover { background: #1eb854; transform: scale(1.02); }
    #hub-modal {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.7);
      z-index: 1000000;
      align-items: center;
      justify-content: center;
      font-family: system-ui, sans-serif;
    }
    #hub-modal-content {
      background: #0f172a;
      color: #f8fafc;
      width: 90%;
      max-width: 520px;
      max-height: 80vh;
      border-radius: 14px;
      padding: 24px;
      overflow-y: auto;
      border: 1px solid #334155;
    }
    .hub-link {
      display: block;
      padding: 12px 14px;
      margin-bottom: 8px;
      background: #1e293b;
      border-radius: 8px;
      color: #38bdf8;
      text-decoration: none;
      font-size: 14px;
      font-weight: 600;
    }
    .hub-link:hover { background: #334155; color: white; }
  `;
  document.head.appendChild(style);

  // Floating Hub Badge
  const badge = document.createElement('div');
  badge.id = 'hub-badge';
  badge.innerHTML = '⚡ 20+ Free Tools';
  document.body.appendChild(badge);

  // Floating WhatsApp One-Click Forward Trigger
  const shareBtn = document.createElement('a');
  shareBtn.id = 'hub-share-btn';
  shareBtn.innerHTML = '📲 Share Tool';
  shareBtn.href = 'javascript:void(0)';
  shareBtn.onclick = function() {
    const title = encodeURIComponent(document.title || "Free Online Web Tool");
    const link = encodeURIComponent(window.location.href);
    window.open("https://api.whatsapp.com/send?text=" + "Check out this free tool: " + title + " 👉 " + link, "_blank");
  };
  document.body.appendChild(shareBtn);

  // Modal
  const modal = document.createElement('div');
  modal.id = 'hub-modal';
  modal.innerHTML = `
    <div id="hub-modal-content">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
        <h3 style="margin:0; font-size:18px;">⚡ Digital Utility Suite</h3>
        <span id="hub-close" style="cursor:pointer; font-size:24px; color:#94a3b8;">&times;</span>
      </div>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/exam-resizer/">📷 Sarkari Photo & Signature Resizer</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/sarkari-alert-ai/">📢 Sarkari Alert AI</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/krutidev-unicode-converter/">⌨️ Krutidev to Unicode Converter</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/hindi-typing-tutor/">🇮🇳 Hindi Typing Tutor</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/commerce-accounts-hub/">📚 CBSE Accountancy Solutions</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/pdf-smart-tools/">📄 PDF Smart Tools</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/upi-qr-standee/">💳 UPI QR Standee Maker</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/wa-direct/">💬 WhatsApp Direct Chat</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/loan-emi-calculator/">📊 Loan EMI Calculator</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/panchang-choghadiya/">🕉️ Panchang & Choghadiya</a>
      <a class="hub-link" href="https://unknownuniversem-blip.github.io/" style="text-align:center; background:#0284c7; color:white; margin-top:12px;">🌟 View All 22+ Tools</a>
    </div>
  `;
  document.body.appendChild(modal);

  badge.onclick = () => modal.style.display = 'flex';
  document.getElementById('hub-close').onclick = () => modal.style.display = 'none';
  modal.onclick = (e) => { if (e.target === modal) modal.style.display = 'none'; };
})();
