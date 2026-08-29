package com.jd7.aiadaptive.monitor

data class DeviceSnapshot(
    val timestamp: Long,
    val memoryTotalMb: Long,
    val memoryAvailableMb: Long,
    val batteryPercent: Int,
    val batteryTemperatureC: Float?,
    val storageTotalBytes: Long,
    val storageFreeBytes: Long,
    val thermalStatus: Int?,
    val cpuLoadPercent: Float?
)
