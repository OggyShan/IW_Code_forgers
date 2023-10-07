using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using Python.Runtime;
using Oasis;
namespace Oasis
{

    public partial class ChatWindow : Window
    {
        public class Message : INotifyPropertyChanged
        {
            private string text;
            public string Text
            {
                get { return text; }
                set
                {
                    text = value;
                    OnPropertyChanged("Text");
                }
            }

            public int Column { get; set; }
            public double messege_width { get; set; }

            public event PropertyChangedEventHandler PropertyChanged;

            protected virtual void OnPropertyChanged(string propertyName)
            {
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
            }
        }

        public ObservableCollection<Message> Messages { get; set; } = new ObservableCollection<Message>();

        public void AddUserMessage(string text)
        {
            Messages.Add(new Message { Text = text, Column = 1 });

            //this.DataContext = this;
        }
        public void AddBotMessage(string text)
        {
            Messages.Add(new Message { Text = text, Column = 0 });

            //this.DataContext = this;
        }
        public async Task AddBotMessageAsync(string text)
        {
            var message = new Message { Text = "", Column = 0 };
            Messages.Add(message);

            foreach (char letter in text)
            {
                await System.Windows.Application.Current.Dispatcher.InvokeAsync(() =>
                {
                    message.Text += letter;
                });
                await Task.Delay(15);
            }
        }
        public async Task AddUserMessageAsync(string text)
        {
            var message = new Message { Text = "", Column =  1};
            Messages.Add(message);

            foreach (char letter in text)
            {
                await System.Windows.Application.Current.Dispatcher.InvokeAsync(() =>
                {
                    message.Text += letter;
                });
                await Task.Delay(10);
            }
        }
        private void Messages_CollectionChanged(object sender, System.Collections.Specialized.NotifyCollectionChangedEventArgs e)
        {
            this.Dispatcher.Invoke(() =>
            {
                ChatScrollViewer.ScrollToEnd();
            });
        }
        public ChatWindow()
        {
            if (!PythonEngine.IsInitialized)
            {
                Runtime.PythonDLL = @"C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\python39.dll";
                PythonEngine.Initialize();
            }
            InitializeComponent();
            Messages.CollectionChanged += Messages_CollectionChanged;
            this.DataContext = this;
            double height = SystemParameters.PrimaryScreenHeight;
            double width = SystemParameters.PrimaryScreenWidth;
            double chat_height = (65 * height) / 100;
            double chat_width = (25 * width) / 100;
            this.WindowStartupLocation = WindowStartupLocation.Manual;
            this.ResizeMode = ResizeMode.NoResize;
            this.Height = chat_height;
            this.Width = chat_width;
            this.Left = (width - chat_width) + ((1.5 * Width) / 100);
            this.Top = ((height - chat_height) - ((4.7 * height) / 100));
            this.Topmost = true;
        }
        


        public async void EnterKey(object sender, RoutedEventArgs e)
        {

            if ((e is KeyEventArgs keyEvent && keyEvent.Key == Key.Return) || (sender is Button))
            {
                string query = bottom_query.Text;
                bottom_query.Clear();
                await AddUserMessageAsync(query);
                
                using (Py.GIL())
                {
                    var pyScript = Py.Import("main");
                    var inputString = new PyString(query);
                    var result = pyScript.InvokeMethod("main", new PyObject[] { inputString });

                    string res = result.ToString();
            
                    AddBotMessage(res);
                }


            }

        }
    }
}
