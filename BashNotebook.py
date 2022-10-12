# Databricks notebook source
# MAGIC %sh
# MAGIC echo "Starting on bash"
# MAGIC my_function () {
# MAGIC   echo "My function was called";
# MAGIC }
# MAGIC my_function

# COMMAND ----------

# MAGIC %sh 
# MAGIC my_function

# COMMAND ----------

# MAGIC %sh ls

# COMMAND ----------

# MAGIC %sh source bash_module.sh
# MAGIC hello_world

# COMMAND ----------

# MAGIC %sh hello_world

# COMMAND ----------

# MAGIC %sh ./bash_module.sh

# COMMAND ----------

# MAGIC %sh curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# COMMAND ----------

# MAGIC %sh az --help

# COMMAND ----------

# MAGIC %sh pip install databricks-cli

# COMMAND ----------

# MAGIC %sh databricks --help

# COMMAND ----------


