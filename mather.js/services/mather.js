const messages = require("../proto/mather_pb");

module.exports = {
  add: (call, callback) => {
    const reply = new messages.AddOutputMessage();

    reply.setSum(
      call.request.getFirstsummand() + call.request.getSecondsummand()
    );

    callback(null, reply);
  },
};
