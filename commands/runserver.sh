cd ~/codenjoy/CodingDojo/server
mvn clean spring-boot:run -DMAVEN_OPTS=-Xmx1024m -Dmaven.test.skip=true -Dspring.profiles.active=sqlite,loderunner,debug -Dcontext=/codenjoy-contest -Dserver.port=8080 -Ploderunner
cd -