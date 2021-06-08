const messages = require("../proto/mather_pb");

module.exports = (multiplier) => ({
  add: (call, callback) => {
    const reply = new messages.AddOutputMessage();

    reply.setSum(
      (call.request.getFirstsummand() + call.request.getSecondsummand()) *
        multiplier
    );

    callback(null, reply);
  },
});
