# Agentic AI: Foundations and Open-Source Practice

## Overview

This project demonstrates the basic concepts of Agentic AI using three different approaches:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

The project shows how an AI system can move from simple conversation to tool-based and multi-step task handling.

## Objective

The main objective is to understand the difference between a plain chatbot, a rule-based workflow, and an AI agent.

The project also demonstrates how an AI agent can use tools and an execution loop to handle tasks.

## Approaches

### 1. Plain Chatbot

The plain chatbot uses a Large Language Model (LLM) to understand a user's question and generate a response.

It mainly focuses on conversation and does not perform external actions unless additional tools are provided.

### 2. Rule-Based Workflow

The rule-based workflow follows predefined steps and conditions.

For example, it can check course information and calculate fees using fixed rules. It provides predictable results but has limited flexibility.

### 3. AI Agent

The AI agent combines an LLM with tools and a task execution process.

It can use available tools to retrieve information, perform calculations, and generate a final response based on the results.

## Example Tasks

The project includes examples such as:

* Checking course fees
* Applying a scholarship percentage
* Calculating the final payable amount
* Generating a welcome response

## Technologies Used

* Python
* OpenAI Python SDK
* Groq API
* Python-dotenv
* Git
* GitHub

## Project Files

* `chatbot.py` — Plain chatbot implementation
* `workflow.py` — Rule-based workflow
* `tools.py` — Tools used by the agent
* `agent.py` — AI agent implementation
* `challenge.py` — Challenge implementation
* `config.py` — Configuration and environment setup
* `requirements.txt` — Python dependencies
* `.gitignore` — Files excluded from Git
* `.env` — Local API configuration

## Key Learning

This project demonstrates the basic idea of an AI agent:

**Agent = LLM + Tools + Loop**

A plain chatbot mainly generates responses, while an AI agent can use tools and perform multiple steps to complete a task.

## Conclusion

The project provides a practical introduction to Agentic AI concepts and shows how different approaches can be used for different types of tasks.
