#!/usr/bin/python3 -B

import asyncio
import moteus
import time

async def main():
    qr = moteus.QueryResolution()
    qr._extra = {
        moteus.Register.CONTROL_POSITION : moteus.F32,
        moteus.Register.CONTROL_VELOCITY : moteus.F32,
        moteus.Register.CONTROL_TORQUE : moteus.F32,
        moteus.Register.POSITION_ERROR : moteus.F32,
        moteus.Register.VELOCITY_ERROR : moteus.F32,
        moteus.Register.TORQUE_ERROR : moteus.F32,
    }

    c = moteus.Controller(query_resolution=qr)

    # Clear any faults
    await c.set_stop()

    # Define the trajectory
    positions = [0.5, 1.0, 1.5, 1.0, 0.5, -0.5, -1.0, -1.5, -1.0, -0.5]

    while True:
        for pos in positions:
            results = await c.set_position(
                position=pos,
                velocity=0.0,
                accel_limit=8.0,
                velocity_limit=3.0,
                query=True,
            )
            print(f"Moved to position {pos}: {results}")
            await asyncio.sleep(0.02)  # 1 second delay

if __name__ == '__main__':
    asyncio.run(main())
