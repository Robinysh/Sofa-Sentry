uv run yolo export \
  model=yolo11n.pt \
  format=onnx   \
  device=cpu    \
  simplify=True \
  dynamic=False

uv run yolo export \
  model=yolo11n-seg.pt \
  format=onnx   \
  device=cpu    \
  simplify=True \
  dynamic=False
