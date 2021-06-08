const services = require("./proto/mather_grpc_pb");
const grpc = require("@grpc/grpc-js");
const matherService = require("./services/mather");

let laddr = process.env.LADDR;
if (!laddr) {
  laddr = "0.0.0.0:5000";
}

const server = new grpc.Server();
server.addService(services.MatherService, matherService);
server.bindAsync(laddr, grpc.ServerCredentials.createInsecure(), () => {
  console.log(`Listening on ${laddr}`);

  server.start();
});
