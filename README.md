Introduction
This is an automated Call Bombing and SMS Bombing tool designed for testing and educational purposes. The script enables users to test the resilience of APIs, evaluate spam detection mechanisms, or study API vulnerabilities. It executes the bombing operations with predefined hardcoded parameters for multiple target numbers without requiring user input.
-------------------------------------------------------------------------
Features
Automated Execution:

Runs call bombing first, followed by SMS bombing.
No manual input required for execution.
Multi-Target Support:

Bombs multiple predefined numbers simultaneously.
Predefined Parameters:

Call Bombing:
Calls per target: 5
Delay between calls: 30 seconds
Threads: 1
SMS Bombing:
SMS per target: 5
Delay between SMS: 10 seconds
Threads: 50
Status Tracking:

Real-time display of attempts, successful deliveries, and failures.
Fully Configurable:

Modify hardcoded parameters to fit specific needs.

-----------------------------------------------------------------------------
Prerequisites
Python 3.x installed on your system.
Required Python libraries: requests, colorama.
A stable internet connection.
-----------------------------------------------------------------------------------
Installation

Clone the repository:
git clone https://github.com/vinayhr5/TbombModified.git
cd BombingTool

Install dependencies:
pip install -r requirements.txt

----------------------------------------------------------------------------
Usage
Run the script:
python bomber.py

The bombing process will execute with predefined parameters:
Call bombing starts first.

Once completed, SMS bombing begins automatically.

------------------------------------------------------------------------------

Contributors
Developer: SpeedX
Contributors: t0xic0der, scpketer, Stefan
