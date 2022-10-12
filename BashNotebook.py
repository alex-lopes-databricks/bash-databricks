# Databricks notebook source
# MAGIC %sh
# MAGIC echo "Starting on bash"
# MAGIC my_function () {
# MAGIC   print "My function was called";
# MAGIC }
# MAGIC my_function

# COMMAND ----------

# MAGIC %sh 
# MAGIC my_function

# COMMAND ----------

dbutils.fs.ls("/")

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


