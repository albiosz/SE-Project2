#FROM eclipse-temurin:21-jdk-alpine AS builder
#WORKDIR /app
#COPY mvnw pom.xml ./
#COPY .mvn .mvn
#COPY src src
#RUN ./mvnw clean install -DskipTests


FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
#COPY --from=builder /app/target/*.jar app.jar
COPY ./target/currency_converter-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8081
CMD ["java", "-jar", "app.jar"]