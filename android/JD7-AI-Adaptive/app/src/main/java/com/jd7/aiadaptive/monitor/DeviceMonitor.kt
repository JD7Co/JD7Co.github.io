package com.jd7.aiadaptive.monitor

import android.app.ActivityManager
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.os.BatteryManager
import android.os.Build
import android.os.Environment
import android.os.PowerManager
import android.os.StatFs

class DeviceMonitor(private val context: Context) {

    fun snapshot(): DeviceSnapshot {
        val memory = memoryInfo()
        val battery = batteryInfo()
        val storage = storageInfo()
        val thermal = thermalStatus()

        return DeviceSnapshot(
            timestamp = System.currentTimeMillis(),
            memoryTotalMb = memory.first,
            memoryAvailableMb = memory.second,
            batteryPercent = battery.first,
            batteryTemperatureC = battery.second,
            storageTotalBytes = storage.first,
            storageFreeBytes = storage.second,
            thermalStatus = thermal,
            cpuLoadPercent = null
        )
    }

    private fun memoryInfo(): Pair<Long, Long> {
        val manager = context.getSystemService(ActivityManager::class.java)
        val info = ActivityManager.MemoryInfo()
        manager.getMemoryInfo(info)
        return info.totalMem / MB to info.availMem / MB
    }

    private fun batteryInfo(): Pair<Int, Float?> {
        val manager = context.getSystemService(BatteryManager::class.java)
        val percent = manager.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
        val intent = context.registerReceiver(
            null,
            IntentFilter(Intent.ACTION_BATTERY_CHANGED)
        )
        val rawTemperature = intent?.getIntExtra(
            BatteryManager.EXTRA_TEMPERATURE,
            Int.MIN_VALUE
        )
        val temperature = if (rawTemperature == null || rawTemperature == Int.MIN_VALUE) {
            null
        } else {
            rawTemperature / 10f
        }
        return percent.coerceIn(0, 100) to temperature
    }

    private fun storageInfo(): Pair<Long, Long> {
        val stat = StatFs(Environment.getDataDirectory().path)
        return stat.totalBytes to stat.availableBytes
    }

    private fun thermalStatus(): Int? {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.Q) return null
        val power = context.getSystemService(PowerManager::class.java)
        return power.currentThermalStatus
    }

    private companion object {
        const val MB = 1024L * 1024L
    }
}
