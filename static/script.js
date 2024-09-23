document.addEventListener('DOMContentLoaded', function() {
    const filterButton = document.getElementById('filterButton');
    const fetchDataButton = document.getElementById('fetchDataButton');
    const updateSignalsButton = document.getElementById('updateSignalsButton');
    let dataTable;

    // Initialize sliders and inputs
    const sliders = [
        { 
            slider: document.getElementById('hisseAdetSlider'),
            min: document.getElementById('hisseAdetMin'),
            max: document.getElementById('hisseAdetMax'),
            range: { min: 0, max: 10000000000 }
        },
        { 
            slider: document.getElementById('fiyatPuanSlider'),
            min: document.getElementById('fiyatPuanMin'),
            max: document.getElementById('fiyatPuanMax'),
            range: { min: 1, max: 100 }
        },
        { 
            slider: document.getElementById('pdDdPuanSlider'),
            min: document.getElementById('pdDdPuanMin'),
            max: document.getElementById('pdDdPuanMax'),
            range: { min: 1, max: 100 }
        }
    ];

    sliders.forEach(item => {
        noUiSlider.create(item.slider, {
            start: [item.range.min, item.range.max],
            connect: true,
            range: item.range,
            format: {
                to: function (value) {
                    return Math.round(value);
                },
                from: function (value) {
                    return Number(value);
                }
            }
        });

        // Update input values when slider changes
        item.slider.noUiSlider.on('update', function (values, handle) {
            item.min.value = values[0];
            item.max.value = values[1];
        });

        // Update slider when input values change
        item.min.addEventListener('change', function () {
            item.slider.noUiSlider.set([this.value, null]);
        });

        item.max.addEventListener('change', function () {
            item.slider.noUiSlider.set([null, this.value]);
        });
    });

    function initDataTable(data) {
        if (dataTable) {
            dataTable.destroy();
        }

        const priorityColumns = ['ticker', 'fiyat', 'fiyat_puan', 'pd_dd_puan'];
        const reorderedColumns = [
            ...priorityColumns,
            ...data.columns.filter(col => !priorityColumns.includes(col))
        ];

        const columns = reorderedColumns.map(column => ({
            title: column,
            data: function(row) {
                return Array.isArray(row) ? row[data.columns.indexOf(column)] : row[column];
            },
            render: function(data, type, row, meta) {
                if (type === 'display') {
                    if (column === 'fiyat_puan' || column === 'pd_dd_puan') {
                        const value = parseFloat(data);
                        if (!isNaN(value)) {
                            const color = getColorForValue(value);
                            return `<span style="color: ${color}">${value.toFixed(2)}</span>`;
                        }
                    }
                }
                return data !== undefined ? data : '';
            }
        }));

        dataTable = $('#stockTable').DataTable({
            data: data.stocks,
            columns: columns,
            order: [],
            pageLength: 25
        });
    }

    function getColorForValue(value) {
        const red = Math.max(0, Math.min(255, Math.round(255 * (100 - value) / 100)));
        const green = Math.max(0, Math.min(255, Math.round(255 * value / 100)));
        return `rgb(${red}, ${green}, 0)`;
    }

    function updateTable(data) {
        if (Array.isArray(data) && !data.columns) {
            const columns = data[0];
            const stocks = data.slice(1);
            data = { columns, stocks };
        }
        initDataTable(data);
    }

    function applyFilters() {
        const filters = {
            hisse_adet: sliders[0].slider.noUiSlider.get().join(','),
            fiyat_puan: sliders[1].slider.noUiSlider.get().join(','),
            pd_dd_puan: sliders[2].slider.noUiSlider.get().join(',')
        };
        
        fetch('/filter', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(filters)
        })
        .then(response => response.json())
        .then(data => updateTable(data))
        .catch(error => console.error('Error:', error));
    }
    
    filterButton.addEventListener('click', applyFilters);

    fetchDataButton.addEventListener('click', function() {
        fetch('/fetch_data')
            .then(response => response.json())
            .then(data => updateTable(data))
            .catch(error => console.error('Error:', error));
    });

    updateSignalsButton.addEventListener('click', function() {
        fetch('/update_signals', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Signals updated successfully');
                    fetchDataButton.click();
                } else {
                    alert('Failed to update signals: ' + (data.error || 'Unknown error'));
                }
            })
            .catch(error => console.error('Error:', error));
    });

    // Initial data load
    applyFilters();
});