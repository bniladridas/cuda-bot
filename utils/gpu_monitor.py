import torch

def get_gpu_stats():
    if not torch.cuda.is_available():
        return None

    stats = {
        "device_name": torch.cuda.get_device_name(0),
        "memory_allocated": torch.cuda.memory_allocated() / 1024**2,
        "memory_reserved": torch.cuda.memory_reserved() / 1024**2,
        "temperature": getattr(torch.cuda.get_device_properties(0), 'temperature', "N/A")
    }
    return stats
