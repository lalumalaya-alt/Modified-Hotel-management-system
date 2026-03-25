import re

with open('index.html', 'r') as f:
    text = f.read()

# Let's fix the css class names for the wizard
text = text.replace('<div className="walkin-wizard">', '<div style={{display:"flex", alignItems:"center", justifyContent:"space-between", marginBottom:"20px", background:"#f8f9fa", padding:"15px", borderRadius:"4px", border:"1px solid #dee2e6"}}>')
text = text.replace('<div className={`wizard-step ${walkinStep >= 1 ? \'active\' : \'\'}`}>', '<div style={{flex:1, textAlign:"center", fontWeight:"bold", color: walkinStep >= 1 ? "var(--navy-primary)" : "#aaa"}}>')
text = text.replace('<div className={`wizard-step ${walkinStep >= 2 ? \'active\' : \'\'}`}>', '<div style={{flex:1, textAlign:"center", fontWeight:"bold", color: walkinStep >= 2 ? "var(--navy-primary)" : "#aaa"}}>')
text = text.replace('<div className={`wizard-step ${walkinStep >= 3 ? \'active\' : \'\'}`}>', '<div style={{flex:1, textAlign:"center", fontWeight:"bold", color: walkinStep >= 3 ? "var(--navy-primary)" : "#aaa"}}>')
text = text.replace('<div className="wizard-line"></div>', '<div style={{flex:2, height:"2px", background: "#ddd", margin:"0 10px"}}></div>')

# also fix the form modal-overlay
text = text.replace('<div className="modal-overlay">', '<div className="modal-overlay" onClick={onClose}>')

with open('index.html', 'w') as f:
    f.write(text)
