#!/bin/bash
cd /workspace/backend
pip install -r requirements.txt --break-system-packages
cd /workspace/frontend
npm install
