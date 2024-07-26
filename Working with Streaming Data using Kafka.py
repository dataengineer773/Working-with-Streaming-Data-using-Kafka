# Download Kafka by running the command below:
wget https://downloads.apache.org/kafka/3.7.0/kafka_2.12-3.7.0.tgz


# Extract Kafka from the zip file by running the command below:
tar -xzf kafka_2.12-3.7.0.tgz 


# Configure KRaft and start server :
# Navigate to the kafka_2.12-3.7.0 directory.
cd kafka_2.12-3.7.0


# Generate a cluster UUID that will uniquely identify the Kafka cluster:
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"


# KRaft requires the log directories to be configured. Run the following command to configure the log directories passing the cluster ID:
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties


# Now that KRaft is configured, you can start the Kafka server by running the following command:
bin/kafka-server-start.sh config/kraft/server.properties


# Create a topic and start producer:
# Start a new terminal and change to the kafka_2.12-3.7.0 directory:
cd kafka_2.12-3.7.0


# To create a topic named news, run the command below.
bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092


 
# You need a producer to send messages to Kafka. Run the command below to start a producer:
bin/kafka-console-producer.sh   --bootstrap-server localhost:9092   --topic news


# After the producer starts, and you get the '>' prompt, type any text message and press enter. 
#Or you can copy the text below and paste. The below text sends three messages to Kafka.
Good morning
Good day
Enjoy the Kafka lab



# Start Consumer:
# Start a new terminal and change to the kafka_2.12-3.7.0 directory.
cd kafka_2.12-3.7.0


# Run the command below to listen to the messages in the topic news.
bin/kafka-console-consumer.sh   --bootstrap-server localhost:9092   --topic news   --from-beginning


# Kafka directories
# Start a new terminal and navigate to the kafka_2.12-3.7.0 directory.
cd kafka_2.12-3.7.0



# Explore the root directory of the server.
ls


# Notice there is a tmp directory. The kraft-combine-logs inside the tmp directory contains all the logs.
# To check the logs generated for the topic news run the following command:
ls /tmp/kraft-combined-logs/news-0


# Create a new topic named weather:
bin/kafka-topics.sh --create --topic weather --bootstrap-server localhost:9092


# Post messages to the topic weather:
bin/kafka-console-producer.sh   --bootstrap-server localhost:9092   --topic weather



# Read the messages from the topic weather:
bin/kafka-console-consumer.sh   --bootstrap-server localhost:9092   --topic weather