const { CosmosClient } = require("@azure/cosmos");

const endpoint = process.env.COSMOS_ENDPOINT || "";
const key = process.env.COSMOS_KEY || "";
const client = new CosmosClient({ endpoint, key });

module.exports = async function (context, req) {
    context.log('Saving matrix operation...');

    if (req.body && req.body.user) {
        try {
            // For course work demo, we'll return success even if DB is not configured yet
            // This allows the UI to work immediately
            context.res = {
                status: 200,
                body: { message: "Operation saved successfully (Simulated for demo)", data: req.body }
            };
        } catch (error) {
            context.res = {
                status: 500,
                body: "Error saving to database"
            };
        }
    } else {
        context.res = {
            status: 400,
            body: "Please pass a valid operation data in the request body"
        };
    }
};
