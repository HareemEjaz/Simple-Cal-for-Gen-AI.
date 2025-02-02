{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/HareemEjaz/Simple-Cal-for-Gen-AI./blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true,
          "base_uri": "https://localhost:8080/"
        },
        "id": "aFl_mz44MKbz",
        "outputId": "823ef5c8-5fb4-4043-cdbb-f660b095e9cf"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Select operation:\n",
            "1. Add\n",
            "2. Subtract\n",
            "3. Multiply\n",
            "4. Divide\n",
            "5.0 - 3.0 = 2.0\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "\n",
        "# Function definitions\n",
        "def add(x, y):\n",
        "    return x + y\n",
        "\n",
        "def subtract(x, y):\n",
        "    return x - y\n",
        "\n",
        "def multiply(x, y):\n",
        "    return x * y\n",
        "\n",
        "def divide(x, y):\n",
        "    if y != 0:\n",
        "        return x / y\n",
        "    else:\n",
        "        return \"Cannot divide by zero!\"\n",
        "\n",
        "# Streamlit app layout\n",
        "st.title(\"Simple Calculator\")\n",
        "\n",
        "# User inputs\n",
        "num1 = st.number_input(\"Enter first number:\", format=\"%.2f\")\n",
        "num2 = st.number_input(\"Enter second number:\", format=\"%.2f\")\n",
        "\n",
        "# Operation selection\n",
        "operation = st.selectbox(\"Select operation:\", (\"Add\", \"Subtract\", \"Multiply\", \"Divide\"))\n",
        "\n",
        "# Perform calculation\n",
        "if st.button(\"Calculate\"):\n",
        "    if operation == \"Add\":\n",
        "        result = add(num1, num2)\n",
        "    elif operation == \"Subtract\":\n",
        "        result = subtract(num1, num2)\n",
        "    elif operation == \"Multiply\":\n",
        "        result = multiply(num1, num2)\n",
        "    elif operation == \"Divide\":\n",
        "        result = divide(num1, num2)\n",
        "\n",
        "    st.write(f\"Result: {result}\")\n",
        "import streamlit as st\n",
        "\n",
        "# Function definitions\n",
        "def add(x, y):\n",
        "    return x + y\n",
        "\n",
        "def subtract(x, y):\n",
        "    return x - y\n",
        "\n",
        "def multiply(x, y):\n",
        "    return x * y\n",
        "\n",
        "def divide(x, y):\n",
        "    if y != 0:\n",
        "        return x / y\n",
        "    else:\n",
        "        return \"Cannot divide by zero!\"\n",
        "\n",
        "# Streamlit app layout\n",
        "st.title(\"Simple Calculator\")\n",
        "\n",
        "# User inputs\n",
        "num1 = st.number_input(\"Enter first number:\", format=\"%.2f\")\n",
        "num2 = st.number_input(\"Enter second number:\", format=\"%.2f\")\n",
        "\n",
        "# Operation selection\n",
        "operation = st.selectbox(\"Select operation:\", (\"Add\", \"Subtract\", \"Multiply\", \"Divide\"))\n",
        "\n",
        "# Perform calculation\n",
        "if st.button(\"Calculate\"):\n",
        "    if operation == \"Add\":\n",
        "        result = add(num1, num2)\n",
        "    elif operation == \"Subtract\":\n",
        "        result = subtract(num1, num2)\n",
        "    elif operation == \"Multiply\":\n",
        "        result = multiply(num1, num2)\n",
        "    elif operation == \"Divide\":\n",
        "        result = divide(num1, num2)\n",
        "\n",
        "    st.write(f\"Result: {result}\")\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN9OFgJ0AXde4NMxGO7Qex4",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}