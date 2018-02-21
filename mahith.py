import pip


class PackageInstallerClass(object):
    """
        Works for INPUT like given example:

        Eg:
                    {
                        Dependencies =
                            {
                                beautifulsoup4==4.4.1,
                                boto==2.48.0,
                                bz2file==0.98,
                                certifi==2017.7.27.1,
                                chardet==3.0.4,
                                gensim==2.3.0,
                                html5lib==0.999,
                                idna==2.5,
                                nltk==3.2.4,
                                numpy==1.13.1,
                                pexpect==4.0.1,
                                pip==9.0.1,
                                ptyprocess==0.5,
                                pyxdg==0.25,
                                reportlab==3.3.0,
                                requests==2.18.3,
                                scipy==0.19.1,
                                setuptools==20.7.0,
                                six==1.10.0,
                                smart-open==1.5.3,
                                textblob==0.12.0,
                                twitter==1.17.1,
                                urllib3==1.22,
                            },
                    }

    """

    def __init__(self):
        self.json_file_txt_path = "/home/kolukuri/Videos/analytics_regression_Thurs15/analytics_regression/inputs_text.json"

    def parse_input_file_fn(self):
        with open(self.json_file_txt_path, 'r') as input_file:
            try:
                json_f = input_file.read()
                json_f = json_f.replace('{', '\n')
                json_f = json_f.replace('}', '\n')
                json_f = json_f.replace(',', '\n')
                return json_f
            except ValueError as e:
                print('invalid json: %s' % e)
                return None

    def main(self):
        output = self.parse_input_file_fn()
        summary_dict = {'success': [], 'fail': []}
        for i in output.splitlines():
            if "==" in i:
                status = pip.main(['install', i])
                print status
                if status == 0:
                    print "%s : Module installed successfully" % i
                    summary_dict['success'].append(i)
                else:
                    print "%s : Module failed to install" % i
                    summary_dict['fail'].append(i)
        print summary_dict
        for k, dependency_list in summary_dict.items():
            print "-"*20, k, " dependencies", "-"*20
            for enum, dependency in enumerate(dependency_list, 1):
                print enum, ". ", dependency


if __name__ == '__main__':
    abc = PackageInstallerClass()
    abc.main()
