<h1 align="center">
    <img alt="dwin Logo" width="350px" src="logo/dwin_logo.png"><br>
</h1>

<div align="center">
<i style="display: block; font-style: italic; font-size:15px;">Cache Library for API Services 🚀</i>
</div>

## Details 🚀
Welcome to **dwin**, a robust and lightweight caching library for Python, designed to enhance the performance and efficiency of your API interactions. Leveraging the simplicity and reliability of SQLite, Dwin provides a persistent, disk-based cache for API responses, making it an ideal choice for applications where quick and reliable data retrieval is crucial.



## Features 🌟

- **Persistent API Response Caching**: Utilizes SQLite for durable, disk-based caching.
- **Automatic Cache Management**: Handles insertion, retrieval, and expiration of cache data seamlessly.
- **Easy to Integrate**: Designed to be simple to set up and use within your existing Python applications.
- **Customizable Expiry Policy**: Allows for flexible cache expiration settings to suit various use cases.
- **Lightweight**: No heavy dependencies or complex server setups required.

## Getting Started 🚀
Below you'll find a quick guide on how to get started with Dwin. For more detailed instructions, please refer to the full documentation.

### Installation 

Install Dwin using pip:

```bash
pip install dwin
```

### Basic Usage

Here's a simple example of how to use Dwin to cache API responses:

```python
from dwin import DwinCache

# Create a cache instance
cache = DwinCache(db_path='path/to/your/cache.db')

# Fetch data with caching
url = "https://api.example.com/data"
response = cache.fetch(url)
print(response)


```

### Advanced Usage 🛠

`dwin` also supports advanced features like custom expiration times, namespace partitioning, and more. Here's how you can leverage these features:

```python
from dwin import DwinCache

# Initialize the cache with a custom expiration time (in seconds)
cache = DwinCache(db_path='path/to/your/cache.db', expire_after=1800)

# Manually managing cache
cache.set('custom_key', 'Cached content')
cached_content = cache.get('custom_key')
print(cached_content)


```

## Contributing 🤝

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

- Fork the Project

- Create your Feature Branch (`git checkout -b feature/AmazingFeature`)

- Commit your Changes (`git commit -m 'Add some AmazingFeature`)

- Push to the Branch (`git push origin feature/AmazingFeature`)

- Open a Pull Request

## License 📄
Dwin is released under the MIT License. See the bundled LICENSE file for details.

## Support 💬
If you encounter any problems or have any queries about Dwin, please feel free to create an issue or contact us through our support channels.