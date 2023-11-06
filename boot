<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <title>Simple Responsive Page</title>

    <style>
        /* Custom CSS styles */
        body {
            background-color: #f0f0f0;
        }

        h1 {
            color: #333;
        }

        p {
            font-size: 16px;
        }

        /* Add more custom styles as needed */
    </style>
</head>
<body>
    <div class="container">
        <h1>My Responsive Page</h1>
        <p>This is a simple responsive page built with Bootstrap.</p>

        <div class="row">
            <div class="col-md-6">
                <h2>Column 1</h2>
                <form>
                    <div class="mb-3">
                        <label for="username">Username</label>
                        <input type="text" id="username" class="form-control" placeholder="Enter your username">
                    </div>
                    <div class="mb-3">
                        <label for="password">Password</label>
                        <input type="password" id="password" class="form-control" placeholder="Enter your password">
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
            <div class="col-md-6">
                <h2>Column 2</h2>
                <p>Some content in the second column.</p>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script>
</body>
</html>
