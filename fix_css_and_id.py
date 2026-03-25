import re

with open('index.html', 'r') as f:
    text = f.read()

# 1. Fix modal styling
text = text.replace('<div className="modal-content" style={{maxWidth: \'1200px\'}}>',
                    '<div className="modal modal-wide" onClick={e=>e.stopPropagation()}>\n            <div className="modal-header">')

text = text.replace('<button className="close-btn" onClick={onClose}><i className="fas fa-times"></i></button>\n            <h3 style={{marginBottom: \'20px\', color: \'var(--navy-primary)\'}}>',
                    '<h3 style={{color: \'var(--navy-primary)\'}}>\n              <i className={mode===\'advance\'?\'fas fa-calendar-check\':\'fas fa-walking\'}></i> \n              {editRowIndex ? \' Edit Check-In\' : mode===\'advance\' ? \' Advance Booking Check-In\' : \' Walk-In Check-In\'}\n            </h3>\n            <button type="button" className="close-btn" onClick={onClose}><i className="fas fa-times"></i></button>\n          </div>\n          <div className="modal-body">')

text = text.replace('<i className={mode===\'advance\'?\'fas fa-calendar-check\':\'fas fa-walking\'}></i> \n              {editRowIndex ? \' Edit Check-In\' : mode===\'advance\' ? \' Advance Booking Check-In\' : \' Walk-In Check-In\'}\n            </h3>', '')

text = text.replace('</form>\n          </div>\n        </div>', '</form>\n          </div>\n        </div>\n      </div>')

# 2. Add Identity Proof back
text = text.replace('<div className="form-group"><label>Mobile *</label><input type="text" className="form-control" value={fd.mobile} onChange={e=>setFd({...fd,mobile:e.target.value})} required/></div>',
                    '<div className="form-group"><label>Identity Proof</label><input type="text" className="form-control" value={fd.identityProof} onChange={e=>setFd({...fd,identityProof:e.target.value})} placeholder="ID/Passport Number" /></div>\n                        <div className="form-group"><label>Mobile *</label><input type="text" className="form-control" value={fd.mobile} onChange={e=>setFd({...fd,mobile:e.target.value})} required/></div>')

with open('index.html', 'w') as f:
    f.write(text)
