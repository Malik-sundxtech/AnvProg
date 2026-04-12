"""Fake sensors for generating realistic measurements from different sensor types.

Supports: PPG (heart rate), BloodPressure (systolic/diastolic), Temperature.
Creates mostly valid values with ~2% sensor noise/errors.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import random
from typing import Optional


@dataclass
class Measurement:
    value: float
    timestamp_ns: int
    valid_min: float = None
    valid_max: float = None

    def __repr__(self) -> str:
        return f"Measurement(value={self.value}, timestamp_ns={self.timestamp_ns})"
    
    def is_valid(self) -> bool:
        """Check if measurement value is within valid range."""
        if self.valid_min is None or self.valid_max is None:
            return True
        return self.valid_min <= self.value <= self.valid_max


class FakeSensor:
    """Generate realistic measurements from different sensor types.
    
    Supported types: 'PPG' (40-200 bpm), 'BloodPressure' (90-180 mmHg systolic), 'Temperature' (35-42°C)
    """
    
    def __init__(self, sensor_id: str, sensor_type: str = 'PPG', force_success: bool = False) -> None:
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type.upper()

        # Define valid range and jitter for each sensor type
        match self.sensor_type:
            case "PPG":
                # Heart rate: typical 40-200 bpm, jitter ±3
                self.valid_min, self.valid_max = 10, 250
                self._jitter_range = 3
            case "BLOODPRESSURE":
                # Systolic blood pressure: typical 50-200 mmHg, jitter ±5 mmHg
                self.valid_min, self.valid_max = 0, 250
                self._jitter_range = 5
            case "TEMPERATURE":
                # Temperature: typical 35-42°C, jitter ±0.3°C
                self.valid_min, self.valid_max = 32.0, 45.0
                self._jitter_range = 0.3
            case _:
                raise ValueError(
                    f"Unknown sensor type: {sensor_type}. "
                    f"Supported types: 'PPG', 'BloodPressure', 'Temperature'"
                )
        
        self._last_value = random.uniform(
            self.valid_min, 
            self.valid_min + (self.valid_max - self.valid_min) * 0.3
        )
        if force_success:
            self.__measurement_failure_rate = random.uniform(0.0, 0.4) 
        else:
            self.__measurement_failure_rate = random.uniform(0.0, 0.06)  # Default ~2% invalid

    def _generate_value(self, invalid: bool) -> float:
        """Generate a measurement value, optionally invalid (sensor noise)."""
        if invalid:
            # Generate invalid value outside valid range
            if random.random() < 0.5:
                # Below valid_min
                return self.valid_min - random.uniform(1, 100)
            else:
                # Above valid_max
                return self.valid_max + random.uniform(1, 100)
        
        # Generate valid value with jitter from last value
        jitter = random.uniform(-self._jitter_range, self._jitter_range)
        new_value = self._last_value + jitter
        
        # Clamp to valid range
        new_value = max(self.valid_min, min(self.valid_max, new_value))
        return new_value

    def measure(self) -> Measurement:
        """Get one measurement from the sensor."""
        invalid = random.random() < self.__measurement_failure_rate  # ~2% invalid
        value = self._generate_value(invalid=invalid)
        
        # Only update baseline for valid measurements
        if not invalid:
            self._last_value = value
        
        return Measurement(
            value=round(value, 2),
            timestamp_ns=int(datetime.now().timestamp() * 1e9),
            valid_min=self.valid_min,
            valid_max=self.valid_max
        )


if __name__ == "__main__":
    # Demo: Generate measurements from different sensor types
    for sensor_type in ["PPG", "BloodPressure", "Temperature"]:
        print(f"\n=== {sensor_type} Sensor ===")
        sensor = FakeSensor(sensor_id="dev-001", sensor_type=sensor_type)
        measurements = [sensor.measure() for _ in range(10)]
        
        valid = [m for m in measurements if m.is_valid()]
        invalid = [m for m in measurements if not m.is_valid()]
        
        print(f"Valid measurements: {len(valid)}/{len(measurements)}")
        print(f"Invalid (noise): {len(invalid)}/{len(measurements)}")
        print("First 5 measurements:")
        for m in measurements[:5]:
            print(f"  {m}")
