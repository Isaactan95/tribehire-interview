# tribehire-interview

<h2>Description:</h2>
<ul>
    <li>REST API was created in a simple flask sever in <b>server.py</b></li>
    <li>API consist of 2 pars.
        <ol>
            <li>Get top <b>n</b> posts with the most total comments.
                <ol>
                    <li><b>GET</b> Method <em>(default 5)</em></li>
                    <li><b>POST</b> Method</li>
                </ol>
            </li>
            <li>Filter data with available fields.
                <ol>
                    <li><b>POST</b> Method</li>
                </ol>
            </li>
        </ol>
    </li>
</ul>


<h2>Questions</h2>
<ol>
    <li>Return a list of Top Posts ordered by their number of Comments.
        <ul>
            <li>Endpoint: <code>"/getTop"</code></li>
            <li><b>GET</b> Method</li>
            <li><b>POST</b> Method
                <ul>
                    <li>Content type: <b>JSON</b></li>
                    <li><code>{"data":10}</code> <em>#return 10 results</em></li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Search API Create an endpoint that allows a user to filter the comments based on all the available fields. Your solution needs to be scalable.</li>
    <ul>
    <li>Endpoint: <code>"/filterDataBy"</code></li>
        <li><b>POST</b> Method</li>
        <li>Parameters:
        <ul>
            <li>Content type: <b>JSON</b></li>
            <li><code>{"mode":0, "data":{"email":"biz"}}</code></li>
            <li><code>{"mode":1, "data":{"title":"provident"}}</code></li>
        </ul>
        </li>
        <li>Mode is to switch to comments or post filter. <em>0 = comments, 1 = posts</em></li>
        <li>Data is the filter arguments. If invalid, API will throw some error message as response.</li>
    </ul>
</ol>