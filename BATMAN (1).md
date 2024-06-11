{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b9bce714",
   "metadata": {},
   "source": [
    "# B.A.T.M.A.N. Advanced (batman-adv) Setup Guide"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0e5855a",
   "metadata": {},

   "source": [
    "## Run the Installation Script:"
   ]
  },
  {
   "cell_type": "raw",
   "id": "5b41540d",
   "metadata": {},
   "source": [
    "chmod +x install_batman_adv.sh\n",
    "./install_batman_adv.sh\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c09d63b3",
   "metadata": {},
   "source": [
    "## Running and Testing the Setup"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "716ec6d9",
   "metadata": {},
   "source": [
    "### 1 Load the Kernel Module:\n",
    "\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "cfc407e3",
   "metadata": {},
   "source": [
    "sudo modprobe batman-adv\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ddd73ac",
   "metadata": {},
   "source": [
    "### 2 Add Network Interfaces to batman-adv:"
   ]
  },
  {
   "cell_type": "raw",
   "id": "503ee934",
   "metadata": {},
   "source": [
    "sudo batctl if add <network-interface>\n",
    "\n",
    "sudo ip link set up dev bat0\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1135b040",
   "metadata": {},
   "source": [
    "## Testing Conectivity "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b544da45",
   "metadata": {},
   "source": [
    "## 1 Check the Status of Interfaces:"
   ]
  },
  {
   "cell_type": "raw",
   "id": "12b04720",
   "metadata": {},
   "source": [
    "sudo batctl if\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0dba1917",
   "metadata": {},
   "source": [
    "### 2 Ping Between Nodes:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f309d470",
   "metadata": {},
   "source": [
    "Ensure batman-adv is running on all nodes in your network, then use ping to test connectivity."
   ]
  },
  {
   "cell_type": "raw",
   "id": "a3d7fdf0",
   "metadata": {},
   "source": [
    "ping <other-node-ip>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45c032fc",
   "metadata": {},
   "source": [
    "## Monitoring and Managing the Network"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "244cbf54",
   "metadata": {},
   "source": [
    "### 1 View Routing Table"
   ]
  },
  {
   "cell_type": "raw",
   "id": "32dae393",
   "metadata": {},
   "source": [
    "sudo batctl o\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "084cf3b3",
   "metadata": {},
   "source": [
    "### 2 Check the log: "
   ]
  },
  {
   "cell_type": "raw",
   "id": "b37da1e8",
   "metadata": {},
   "source": [
    "sudo dmesg | grep batman-adv\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "409e6572",
   "metadata": {},
   "source": [
    "## Results Storage"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d2ea884",
   "metadata": {},
   "source": [
    "batman-adv: Routing information and logs can be accessed using batctl commands.\n",
    "\n",
    "batctl: Provides a suite of commands to manage and monitor batman-adv.\n",
    "\n",
    "alfred: Collects and distributes information among nodes, results can be accessed using ' alfred ' commands."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02a490b7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
